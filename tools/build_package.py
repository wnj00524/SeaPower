"""Build the installable archive from the reviewable campaign directory."""
from pathlib import Path
import io
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
buffer = io.BytesIO()
with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for path in sorted((root / 'campaign').rglob('*')):
        if path.is_file():
            entry = zipfile.ZipInfo(path.relative_to(root / 'campaign').as_posix(), date_time=(2026,10,17,0,0,0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
target = root / 'Operation_Broken_Trident_Sea_Power_Alpha_Airbases.zip'
if '--check' in sys.argv:
    if not target.exists() or target.read_bytes() != buffer.getvalue():
        raise SystemExit('Archive is out of date: run python tools/build_package.py')
    print('Archive matches campaign source.')
else:
    target.write_bytes(buffer.getvalue())
    print(f'Built {target.name} ({target.stat().st_size} bytes).')
