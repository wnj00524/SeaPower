"""Validate packaged briefing paths, XML asset bindings and PNG integrity offline."""
import json
import re
import struct
import xml.etree.ElementTree as ET
import zlib
from pathlib import PureWindowsPath

from validate_scenarios import ROOT, read

MOD=ROOT/'campaign/user/Operation_Broken_Trident'


def resolve(value):
    return MOD.joinpath(*PureWindowsPath(value).parts)


def png(path):
    raw=path.read_bytes()
    assert raw[:8]==b'\x89PNG\r\n\x1a\n',f'bad PNG signature: {path}'
    i=8;compressed=[];ended=False
    while i<len(raw):
        size=struct.unpack('>I',raw[i:i+4])[0];tag=raw[i+4:i+8];data=raw[i+8:i+8+size]
        crc=struct.unpack('>I',raw[i+8+size:i+12+size])[0]
        assert zlib.crc32(tag+data)&0xffffffff==crc,f'bad PNG CRC: {path}'
        if tag==b'IHDR':
            width,height,depth,color=struct.unpack('>IIBB',data[:10])
            assert width%4==height%4==0,f'non-DXT-aligned image: {path}'
            assert depth==8 and color==2,f'expected RGB PNG: {path}'
        if tag==b'IDAT':compressed.append(data)
        if tag==b'IEND':ended=True
        i+=12+size
    assert ended and i==len(raw),f'truncated PNG: {path}'
    pixels=zlib.decompress(b''.join(compressed))
    assert len(pixels)==height*(width*3+1),f'incomplete PNG pixels: {path}'


def validate():
    entries=json.loads((ROOT/'briefing_source/missions.json').read_text())
    assert [x['id'] for x in entries]==list(range(1,13))
    paths=sorted(MOD.rglob('missions/*.ini'));assert len(paths)==12
    all_images=set()
    for path in paths:
        c=read(path);s=c['Language_en'];n=int(path.name[:2])
        folder=resolve(s['MissionBriefingAssetsDirectory'])
        assert folder.is_dir(),folder
        assets={p.stem:p for p in folder.iterdir() if p.suffix in ('.png','.jpg')}
        for key in ('MissionBriefingLeftPane','MissionBriefingRightPane'):
            xml=resolve(s[key]);assert xml.is_file(),xml
            ET.parse(xml)
            refs=re.findall(r'Assets\[([^\]]+)\]',xml.read_text())
            assert refs,f'no graphics referenced: {xml}'
            assert all(r in assets for r in refs),f'missing image binding: {xml}'
            all_images.update(assets[r] for r in refs)
        right=resolve(s['MissionBriefingRightPane']).read_text()
        assert f'Assets[chart{n:02}]' in right
        left=resolve(s['MissionBriefingLeftPane']).read_text()
        assert f'Assets[phase{(n-1)//4+1}]' in left
        orders=resolve(s['MissionBriefingLeftPane']).with_name('Orders_en.md')
        assert orders.is_file() and len(orders.read_text().split())>=250
        assert 'MISSION / COMPLETION CONDITIONS' in left and 'RULES OF ENGAGEMENT' in left
        print(path.name+': briefing links and XML PASS')
    assert len(all_images)==15
    for path in all_images:
        if path.suffix=='.png':png(path)
        else:
            raw=path.read_bytes();assert raw[:2]==b'\xff\xd8' and raw[-2:]==b'\xff\xd9',path
    print('12 briefing pairs; 12 charts and 3 illustrations; asset integrity PASS.')


if __name__=='__main__':validate()
