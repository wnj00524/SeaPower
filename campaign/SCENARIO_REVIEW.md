# Reinforced scenario review — 17 October 2026

Status: revised files and installable archive; offline checks passed. **Not run in Sea Power.**

## Geography findings and correction

The original archive did not demonstrate an enemy ship starting on land under the longitude/latitude-arcminute coordinate interpretation. It did contain dangerous authored routes: both mission 1 enemy surface tracks crossed or approached Malta/Gozo (minimum sampled clearance 0.00 and 0.30 NM). The new mission 1 operating centre is 35.45°N, 14.2°E, south of Malta, with revised opposing routes. Its safety-area trigger and convoy route retain their relative relationship.

An additional defect affected friendly aircraft support: relative airbase X offsets used a cosine correction. Interpreted as longitude arcminutes, eight missions placed the friendly airfield offshore in the coastline check. All friendly bases now use explicit `GeoPosition`: Sigonella 37.4017,14.9222; Souda 35.5317,24.1497; Akrotiri 34.5904,32.9879. These coordinates still require model/runway placement inspection in the game.

All unit spawns now use `GeoPosition=latitude,longitude,height`. Sea waypoints remain numeric relative arcminutes: longitude = map-centre longitude + X/60; latitude = map-centre latitude + Z/60. Positive Z is north. The archived developer example's negative-Z/north comment conflicts with observed-game placement research; do not reintroduce a cosine correction.

The bundled validator checks every authored vessel/submarine spawn and every straight route leg at intervals no greater than approximately 0.5 NM, requiring at least 3 NM from the Natural Earth 1:50m coastline. It checks land-unit placement too. All 12 missions pass. This is a regional coastline screen, **not** an engine terrain, bathymetry or dynamic AI path guarantee. No random spawns or formation position overrides were added. Purchased Task Force ship spacing still needs live inspection.

## Enemy and civilian changes

Aircraft counts below are explicit airborne units. Each mission also has four reserve MiG-23MLDs at its enemy airfield; reserves are not included in the airborne count. Existing submarines remain, with the mission 9 Foxtrot upgraded to a Kilo. Mission 9's primary Kynda becomes a Slava. Primary target section IDs and existing victory/failure triggers are preserved.

| Mission | Enemy surface before → after | Airborne before → after | New enemy land units | Neutral vessels after |
|---|---:|---:|---:|---:|
| 01 Sicilian Passage | 2 → 3 | 0 → 2 | 5 | 4 |
| 02 Broken Contact | 1 → 3 | 0 → 4 | 5 | 3 |
| 03 The Narrows | 2 → 3 | 0 → 4 | 5 | 4 |
| 04 Crete Barrier | 1 → 3 | 0 → 4 | 5 | 3 |
| 05 The Black Sea Squadron | 2 → 4 | 2 → 8 | 5 | 3 |
| 06 Steel Rain | 2 → 4 | 3 → 8 | 5 | 3 |
| 07 Lifeline to Cyprus | 2 → 4 | 0 → 8 | 5 | 4 |
| 08 Guard the Oiler | 2 → 4 | 1 → 8 | 5 | 4 |
| 09 Sunken Spear | 2 → 4 | 0 → 8 | 5 | 3 |
| 10 Iron Ring | 3 → 4 | 2 → 8 | 5 | 3 |
| 11 Outbound | 2 → 4 | 0 → 8 | 5 | 4 |
| 12 Broken Trident | 3 → 5 | 3 → 10 | 5 | 3 |

Early missions have two MiG-23MLDs; missions 2–4 add two Tu-16Ks. Later missions have four fighters with a mixed Tu-16K/Tu-22M2 bomber force; the finale has six bombers. Known stock loadouts are `AirToAirLongRange`, `Strike` (Tu-16K) and `AntiShip` (Tu-22M2). Flights approach from separated north/south bearings, with farther-out flights arriving later through travel distance. These are not timed reinforcement spawns or guaranteed synchronized salvos. Airborne aircraft have finite fuel.

Each enemy land component contains a `wp_airbase_1`, complete SA-5 and SA-3 sites, a Silkworm launcher and a P-14 early warning radar. Complete SAM-site prefabs avoid orphan launchers without fire-control radars. Bases are on the Libyan coast, except the Cyprus operation's Syrian detachment. This deliberately changes the fictional premise to allow Soviet expeditionary access; it does not imply historical Soviet bases at those coordinates. Silkworm equipment under Soviet control is likewise fictional. Shore threats protect enemy airfields and approaches; their range does not cover every offshore engagement area. They are not additional compulsory victory targets. Airbase reserves may or may not launch autonomously: the authored airborne opposition does not depend on those launches.

Campaign threat-profile displays and mission descriptions now advertise air and land opposition, including missions that previously showed no such threats. Procurement points and maintenance opportunities are unchanged; the reinforced force mix needs balance testing, especially the no-rearm sequence and finale.

Three independent civilian contacts were added to every mission: freighter A, freighter B and a fishing boat. They cross in both directions at different lateral offsets, with one non-emitting contact. All are neutral and weapons hold. Existing protected NeutralVessel1 IDs and loss triggers remain intact, including the oiler in mission 8. Additional traffic creates identification ambiguity; it is not automatically labelled hostile. No blanket civilian-loss defeat trigger was added, because that would also punish the player when enemy AI sinks ambient traffic. Existing protected-ship loss rules still apply.

## ROE and tactical behaviour

Only supported mission fields are used; no invented CMO-style doctrine subsystem is implied.

| Element | ROE / sensors | Authored behaviour |
|---|---|---|
| Missile attackers | Free, radar initially off | Separate flanking surface routes |
| AAW/ASW screens | Tight, search radars on | Offset screen routes; active sonar on suitable BPK escorts |
| Submarines | Tight, radar/active sonar off | Slow submerged crossing patrol |
| Fighters | Tight, radar on | Back-and-forth airborne patrol routes |
| Bombers | Free, mixed initial radar state | Two bearing axes and varied starting ranges |
| Shore defences | Mixed Tight/Free, SAM/radar emitters on | Static defended aviation and coastal complex |
| Civilians | Hold, mixed radar state | Independent opposing traffic lanes |

`DisableEnemyAIPlayer=False` and `AllowEnemyUnitsAttackPlayer=True` explicitly permit enemy AI. No mission-wide `EnemyWeaponStatus` override masks per-unit ROE. `MissionType=NoMission` is retained for manually routed units: the complexity comes from roles, emissions, weapon state, force composition and routes, not an unverified mission-type enum. Native AI contact classification, surface attacks under weapons-free, route abandonment, defensive reactions and airfield tasking require live verification. Crew skill is mostly Seasoned in later missions; do not assume that guarantees smarter tactical AI.

## Reproducible checks and sources

From the repository root: `python tools/validate_scenarios.py`, `python tools/build_package.py`, then `python tools/build_package.py --check`. The ZIP is generated from `campaign/`; editing the ZIP directly is unsupported. GitHub Actions repeats the validation and source/archive consistency checks.

Source references inspected for field names and stock types/loadouts:

- [Archived developer MissionFileInformation.ini](https://github.com/mikprin/sea_power_editor/blob/main/docs/examples_from_dev/MissionFileInformation.ini): GeoPosition, ROE, sensors, crew values and route syntax.
- [Observed coordinate convention](https://github.com/SEST-HOBBY/Seapower-mods/blob/f1e9638282022b9bacffa74e28d8df72e98e8f41/docs/world-sandbox/work/scope-probes.md): arcminutes and positive-north Z. This is community game evidence, not our own engine test.
- [Archived original aircraft files](https://github.com/SEST-HOBBY/Seapower-mods/tree/f1e9638282022b9bacffa74e28d8df72e98e8f41/mods-source/_vanilla/original/aircraft) and [land-unit files](https://github.com/SEST-HOBBY/Seapower-mods/tree/f1e9638282022b9bacffa74e28d8df72e98e8f41/mods-source/_vanilla/original/land_units): type IDs and loadouts. Verify against the user's installed game version; this archive is not an official compatibility guarantee.
- [Natural Earth coastline](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_land.geojson), source blob recorded in `tools/data/README.md`.
