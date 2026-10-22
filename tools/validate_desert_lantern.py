from pathlib import Path
import configparser,re,sys
root=Path('gulf/user/Operation_Desert_Lantern/campaigns/operation-desert-lantern')
def read(p):
 c=configparser.ConfigParser(interpolation=None);c.optionxform=str;c.read(p,encoding='utf-8-sig');return c
campaign=read(root/'campaign.ini'); errors=[]
if campaign['TaskForceModeDifficulty_Easy']['StartingPoints']!='100000':errors.append('Easy starting points not 100000')
missions=sorted((root/'missions').glob('*.ini'))
if len(missions)!=8:errors.append(f'expected 8 missions, got {len(missions)}')
for p in missions:
 c=read(p);m=c['Mission'];
 if m.get('NumberOfTaskforce1LandUnits')!='1':errors.append(f'{p.name}: friendly airbase missing')
 if m.get('NumberOfTaskforce2LandUnits')!='8':errors.append(f'{p.name}: expected 8 coastal land targets')
 if not all(s in c for s in [f'Taskforce2LandUnit{i}' for i in range(1,9)]):errors.append(f'{p.name}: land unit sections missing')
 for key in ('TaskForceModeAirbasePrepAvailable','TaskForceModeAirbasePrepReadySlots','TaskForceModeAirbasePrepInProgressSlots'):
  if key not in campaign['Mission'+str(int(p.name[:2]))]:errors.append(f'{p.name}: missing {key}')
 for n in range(1,9):
  unit=c[f'Taskforce2LandUnit{n}']; pos=unit.get('GeoPosition','')
  try:lat,lon,alt=pos.split(',');lat=float(lat);lon=float(lon)
  except Exception:errors.append(f'{p.name}: invalid land coordinate {n}');continue
  if not (25<=lat<=28 and 55<=lon<=62):errors.append(f'{p.name}: land target {n} outside Gulf of Oman/Iran coastal bounds: {pos}')
  if alt!='0':errors.append(f'{p.name}: land target {n} is not at terrain surface (altitude token {alt})')
 # Sea spawns must remain south of the Iranian target coastline; coastline/depth still need game-editor checks.
 for name in [s for s in c.sections() if re.fullmatch(r'Taskforce2Vessel[0-9]+',s)]:
  lat=float(c[name]['GeoPosition'].split(',')[0]);
  if not (23.5 <= lat < 25.4): errors.append(f'{p.name}: hostile vessel {name} may spawn on coastal terrain')
 # Static object counts and trigger links.
 for kind,plural in [('Vessel','Vessels'),('Submarine','Submarines'),('Aircraft','Aircraft'),('LandUnit','LandUnits')]:
  for side in ('Taskforce1','Taskforce2','Neutral'):
   expected=int(m.get('NumberOf'+side+plural,'0'))
   actual={s for s in c.sections() if re.fullmatch(side+kind+r'\d+',s)}
   if actual!={side+kind+str(i) for i in range(1,expected+1)}:errors.append(f'{p.name}: {side} {kind} count mismatch')
 print(f'{p.name}: '+('PASS' if not any(p.name in e for e in errors) else 'CHECK'))
print(f'{len(missions)} missions; {len(errors)} issue(s). Coordinate bounds and zero altitude do not replace Mission Editor terrain inspection.')
if errors:print('\n'.join(errors));sys.exit(1)
