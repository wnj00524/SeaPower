"""Offline South Atlantic structure, route and campaign-link checks; not engine QA."""
import json
import re
import sys
from pathlib import Path
import validate_scenarios as common

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'falklands/user/Operation_Southern_Resolve'
CAMPAIGN = BASE / 'campaigns/operation-southern-resolve'
common.POLYGONS = json.loads((ROOT / 'tools/data/falklands-land.geojson').read_text())['coordinates']


def validate():
    issues = []
    campaign = common.read(CAMPAIGN / 'campaign.ini')
    roster = common.read(CAMPAIGN / campaign['TaskForceMode']['RosterFile'])
    files = sorted((CAMPAIGN / 'missions').glob('*.ini'))
    assert len(files) == int(campaign['Missions']['NumberOfMissions']) == 8
    assert campaign['Campaign']['Length'] == '8'
    assert campaign['TaskForceMode']['Enabled'] == 'True'
    for i, path in enumerate(files, 1):
        errors = common.validate(path, revised=False)
        c = common.read(path)
        mission = campaign[f'Mission{i}']
        if BASE / mission['MissionFile'] != path:
            errors.append('campaign mission path mismatch')
        if mission['IsUnlocked'] != str(i == 1):
            errors.append('invalid initial unlock state')
        if i > 1 and mission.get('Parents') != str(i - 1):
            errors.append('broken unlock chain')
        if mission.get('TaskForceModeFinalMission', 'False') != str(i == 8):
            errors.append('invalid final mission marker')
        anchors = [s for s in c if c[s].get('TaskForceModeAnchor') == 'True']
        if anchors != ['Taskforce1Vessel1']:
            errors.append('requires exactly one player vessel anchor')
        for entry in mission['TaskForceModeAllowedRosterUnits'].split('|'):
            typ, *variants = entry.split(',')
            values = next((roster[s][typ] for s in roster if typ in roster[s]), '')
            if not values or not set(variants) <= set(values.split('|')[0].split(',')):
                errors.append('invalid roster choice: ' + entry)
        for s in c:
            if not re.fullmatch(r'Trigger\d+', s):
                continue
            t = c[s]
            refs = t.get('Condition_Units', '').split(',')
            if 'Condition_MinimumUnits' in t and int(t['Condition_MinimumUnits']) > len(refs):
                errors.append(s + ': impossible target count')
            for ref in t.get('Action_DisableTriggers', '').split(','):
                if ref and ref not in c:
                    errors.append(s + ': dangling disabled trigger')
            if 'Action_Victory' in t:
                terminal = {n for n in c if c[n].get('Action_Victory')}
                if set(t.get('Action_DisableTriggers', '').split(',')) != terminal:
                    errors.append(s + ': terminal outcomes can race after resolution')
                if t.get('Action_EnableTriggers') != 'Trigger1':
                    errors.append(s + ': missing mission exit')
        print(path.name + ': ' + ('; '.join(errors) if errors else 'PASS'))
        issues.extend(errors)
    print(f'{len(files)} missions; {len(issues)} issues. Coastline only; depth, AI and play balance require Sea Power.')
    return bool(issues)


if __name__ == '__main__':
    sys.exit(validate())
