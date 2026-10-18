"""Create a deterministic, independently installable Falklands campaign archive."""
from pathlib import Path
import io
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
source = root / 'falklands'
buffer = io.BytesIO()
with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(source.rglob('*')):
        if path.is_file():
            entry = zipfile.ZipInfo(path.relative_to(source).as_posix(), (2026, 10, 18, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
target = root / 'Operation_Southern_Resolve_Sea_Power_Alpha.zip'
if '--check' in sys.argv:
    if not target.exists() or target.read_bytes() != buffer.getvalue():
        raise SystemExit('Archive is out of date: run python tools/build_falklands_package.py')
    print('Falklands archive matches source.')
else:
    target.write_bytes(buffer.getvalue())
    print(f'Built {target.name} ({target.stat().st_size} bytes).')
