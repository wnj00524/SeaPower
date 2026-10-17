"""Offline structural/coastline checks; this does not simulate Sea Power AI or depth.

Relative X/Z are longitude/latitude arcminutes. GeoPosition is lat,lon,height.
Natural Earth coastline is approximate; use the game editor for final acceptance.
"""
import configparser
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLYGONS = json.loads((ROOT / 'tools/data/mediterranean-land.geojson').read_text())['geometry']['coordinates']


def in_ring(x, y, ring):
    inside = False
    for (ax, ay), (bx, by) in zip(ring, ring[1:]):
        if (ay > y) != (by > y) and x < (bx-ax)*(y-ay)/(by-ay)+ax:
            inside = not inside
    return inside


def on_land(lat, lon):
    return any(in_ring(lon, lat, p[0]) and not any(in_ring(lon, lat, r) for r in p[1:]) for p in POLYGONS)


def clearance(lat, lon):
    if on_land(lat, lon):
        return 0.0
    scale = math.cos(math.radians(lat))
    best = float('inf')
    for poly in POLYGONS:
        for ring in poly:
            for (ax, ay), (bx, by) in zip(ring, ring[1:]):
                ax, bx, ay, by = (ax-lon)*60*scale, (bx-lon)*60*scale, (ay-lat)*60, (by-lat)*60
                dx, dy = bx-ax, by-ay
                t = max(0, min(1, -(ax*dx+ay*dy)/(dx*dx+dy*dy))) if dx or dy else 0
                best = min(best, math.hypot(ax+t*dx, ay+t*dy))
    return best


def read(path):
    c = configparser.ConfigParser(interpolation=None)
    c.optionxform = str
    c.read(path, encoding='utf-8-sig')
    return c


def position(value, center, geo=False):
    if geo:
        lat, lon, _ = value.split(',')
        return float(lat), float(lon)
    a, _, b = value.split(',')[:3]
    return center[0]+float(b)/60, center[1]+float(a)/60


def validate(path, revised=True):
    c = read(path)
    errors = []
    center = tuple(float(c['Environment'][k]) for k in ('MapCenterLatitude', 'MapCenterLongitude'))
    m = c['Mission']
    for side in ('Taskforce1', 'Taskforce2', 'Neutral'):
        for kind, plural in [('Vessel','Vessels'), ('Submarine','Submarines'), ('Aircraft','Aircraft'), ('LandUnit','LandUnits'), ('Helicopter','Helicopters')]:
            expected = int(m.get('NumberOf'+side+plural, '0'))
            actual = {s for s in c.sections() if re.fullmatch(side+kind+r'\d+', s)}
            if actual != {side+kind+str(i) for i in range(1, expected+1)}:
                errors.append(f'{side}{plural}: count/section mismatch')
    triggers = {s for s in c.sections() if re.fullmatch(r'Trigger\d+', s)}
    if triggers != {'Trigger'+str(i) for i in range(1,int(m['NumberOfTriggers'])+1)}:
        errors.append('trigger count/section mismatch')
    for name in c.sections():
        u = c[name]
        if 'Type' not in u:
            continue
        if 'GeoPosition' in u and 'RelativePositionInNM' in u:
            errors.append(f'{name}: ambiguous spawn')
        start = position(u.get('GeoPosition', u.get('RelativePositionInNM','0,0,0')), center, 'GeoPosition' in u)
        if 'LandUnit' in name:
            if not on_land(*start):
                errors.append(f'{name}: land unit offshore at {start}')
        if 'Vessel' in name or 'Submarine' in name:
            points = [start]+[position(v, center) for v in u.get('Waypoints','').split('|') if v]
            samples = [start]
            for a,b in zip(points,points[1:]):
                n=max(1, math.ceil(math.hypot((a[0]-b[0])*60,(a[1]-b[1])*50)*2))
                samples += [(a[0]+(b[0]-a[0])*i/n, a[1]+(b[1]-a[1])*i/n) for i in range(1,n+1)]
            minimum = min(clearance(*p) for p in samples)
            if minimum < 3:
                errors.append(f'{name}: spawn/route shore clearance {minimum:.2f} NM (<3)')
        if revised and name.startswith('Taskforce2') and u.get('WeaponStatus') not in ('Tight','Free'):
            errors.append(f'{name}: missing combat ROE')
        if name.startswith('Neutral') and u.get('WeaponStatus') != 'Hold':
            errors.append(f'{name}: civilian weapons must be held')
    for name in triggers:
        for key in ('Condition_Units','Action_Units','Action_EnableTriggers'):
            for ref in c[name].get(key,'').split(','):
                if ref and ref not in c:
                    errors.append(f'{name}/{key}: dangling {ref}')
    if revised:
        if c.get('Debug', 'DisableEnemyAIPlayer', fallback='False') != 'False':
            errors.append('enemy AI is disabled')
        if sum(c[s].get('Type','').startswith('civ_') for s in c if s.startswith('NeutralVessel')) < 3:
            errors.append('fewer than three civilian vessels')
        if int(m.get('NumberOfTaskforce2LandUnits','0')) < 4:
            errors.append('missing layered shore threats')
        enemies = [c[s] for s in c if re.fullmatch(r'Taskforce2(?:Vessel|Submarine|Aircraft)\d+',s)]
        if {u.get('WeaponStatus') for u in enemies} != {'Tight','Free'}:
            errors.append('no variation in enemy ROE')
    return errors


if __name__ == '__main__':
    paths = sorted((ROOT / 'campaign').rglob('missions/*.ini'))
    count = 0
    for path in paths:
        errors = validate(path, '--baseline' not in sys.argv)
        count += len(errors)
        print(path.name+': '+('; '.join(errors) if errors else 'PASS'))
    print(f'{len(paths)} missions; {count} issues. Coastline only; bathymetry and live AI require game QA.')
    sys.exit(bool(count) or len(paths) != 12)
