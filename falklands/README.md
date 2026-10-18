# Operation Southern Resolve — Falklands 1988

**Structured alpha: statically checked, not played in Sea Power.** Eight missions for Task Force Mode. Independent of Operation Broken Trident; no external unit mod is intended to be required.

## Premise and command

This is an invented October 1988 crisis, not a reconstruction of 1982 or a claim about real governments' intentions. After a fictional Argentine political crisis, a regional military pact supplies the means for another invasion of the Falkland Islands. Argentine forces seize Stanley and establish an occupation garrison before the campaign opens. Cuba supplies advisers, communications specialists, MiG-21 detachments, missile boats and military stores. Venezuela supplies fuel, armed convoy escorts and F-5 aircraft through Argentine staging bases. These are deliberate alternate-history deployments, not historical orders of battle.

Britain leads the response. The player commands a US Navy surface reinforcement group assigned to protect the logistics flank and interrupt the occupation's seaborne support. British carriers, the landing force and ground operations remain off-map. This role uses the stock US Task Force roster without presenting American ship models as accurate Royal Navy ships. The campaign ends with the sea screen broken, not an engine-simulated recapture of Stanley. Argentina is the principal invader throughout; Cuban and Venezuelan participation is represented by actual opposing units and designated military supply ships, not only briefing text.

## Install and start

1. Download and extract `Operation_Southern_Resolve_Sea_Power_Alpha.zip`.
2. Close the game. Copy `user/Operation_Southern_Resolve` into `Sea Power_Data/StreamingAssets/user/Operation_Southern_Resolve`.
3. Enable the mod, open Campaigns and select **Operation Southern Resolve (Falklands - Task Force Mode)**.
4. Start on **Supported**. Purchase at least two escorts; include sonar, a shipborne helicopter and area air defence. No aircraft carrier, free combat aircraft or friendly airbase is provided.
5. If it does not appear, inspect the game log and compare the installed Task Force campaign format with `original/campaigns/pacific-strike-task-force`. ApproximateVersion 0.8.0 follows the repository's existing alpha and is not a tested version guarantee.

Ships, damage and recorded ammunition state use native Task Force persistence. The US roster offers Knox, Perry, Spruance, Adams and Belknap classes. Ship-assigned helicopters are included. There are Supported, Standard and Severe point/repair presets. Aircraft procurement and submarine ownership are disabled; the submarine missions are surface/helo ASW tasks.

## Operations

All dates are fictional October 1988; mission times are UTC. Surface operations remain offshore, north or east of the islands. No passage through Falkland Sound or shallow-water landing track is authored.

| Mission | Date | Primary objective | Rearm / repair |
|---|---|---|---|
| 01 Southern Alarm | 3 Oct | Deliver the evacuation freighter to its marked safety area | Yes |
| 02 Silent Shelf | 6 Oct | Destroy the Argentine submarine north of West Falkland | No |
| 03 Caribbean Lifeline | 9 Oct | Destroy the Venezuelan military supply ship and its escort | Yes |
| 04 Cold Picket | 12 Oct | Keep at least one task-force ship afloat for 60 minutes | No |
| 05 The Long Replenishment | 15 Oct | Deliver the stores ship to the replenishment box | Yes |
| 06 Sever the Bridge | 18 Oct | Destroy the Cuban military transport and Argentine escort | No |
| 07 Open Water | 21 Oct | Destroy the Argentine submarine threatening the logistics route | Yes |
| 08 Southern Resolve | 24 Oct | Destroy the three designated Argentine, Venezuelan and Cuban warships | No |

Other missions have a 180-minute deadline. All fail if the player loses every vessel. Escort missions also fail if their protected freighter sinks; their success requires arrival, not merely waiting. Enemy military transports belong to Taskforce2; unrelated merchants and fishing traffic belong to Neutral with weapons held. Positive identification is required. Terminal triggers disable competing outcomes during the mission-exit delay.

## Equipment abstraction

Only existing base-game type IDs are referenced. Names distinguish fictional operators, but underlying silhouettes, flags, sensors, weapons, handling and skins remain those of the stock units. The generic enemy taskforce nation is `Soviet`, a format-compatible coalition placeholder, not a fourth belligerent. This is a gameplay prototype, not a historically faithful fleet pack.

| Fictional force | Stock representation | Material limitation |
|---|---|---|
| Argentine destroyer | `usn_dd_gearing_fram2` | Generic gun/ASW destroyer proxy |
| Argentine final screen leader | `usn_ddg_adams_late` | Missile-destroyer substitute, not an accurate Type 42 |
| Argentine diesel submarine | `rcn_ss_oberon` | Oberon substitute for an Argentine boat; different sonar and weapon performance |
| Argentine Skyhawk | `ran_a-4g`, Strike | Australian A-4G substitutes for Argentine variants; no Super Etendard/Exocet capability is claimed |
| Cuban missile boats | `wp_ptg_osa2` | Stock Osa II equipment under fictional Cuban deployment |
| Cuban fighter detachment | `wp_mig-21`, AirToAir | Generic stock MiG-21; no faithful Cuban squadron skin claimed |
| Venezuelan escort | `usn_ffg_oliver_hazard_perry` | Perry substitutes for a Lupo-type escort; substantially different systems |
| Venezuelan strike aircraft | `usaf_f-5a`, Strike | Generic F-5A under fictional deployment |
| Military logistics | `civ_ms_freighter_a/b` on enemy side | Hostile military-chartered transport, separate from neutral traffic |

Airborne raids are explicitly authored with finite fuel. Nearer and farther starts spread arrivals by flight time; they are not synchronized scripted launches. Cuban fighters and Venezuelan aircraft are assumed staged via Argentine bases before these short engagements, not flying nonstop from the Caribbean. No friendly shore base is invented on occupied territory. There is no dynamic enemy economy, landing simulation, branching front, persistent enemy damage or simulated Caribbean transit. Generic AI must be checked in game, especially bomb attacks, ship attack selection and finite-fuel recovery without authored airfields.

## Validation and source evidence

Run from repository root with Python 3 and no third-party packages:

```sh
python tools/validate_falklands.py
python tools/build_falklands_package.py
python tools/build_falklands_package.py --check
```

The dedicated validator checks unit counts, references, target counts, roster membership, unlocks, final mission, task-force anchors, terminal trigger exclusion and authored sea routes against the bundled Natural Earth South Atlantic polygons. It samples routes and requires 3 NM coastline clearance. It does not check bathymetry, formation spacing, engine terrain, AI pursuit, weapons effectiveness or balance. Existing Mediterranean checks remain separate.

Format and type/loadout evidence: the repository's existing Task Force campaign, the [archived original game files](https://github.com/SEST-HOBBY/Seapower-mods/tree/5b5ace261727d60c3b2530e2bf9afb170258f89a/mods-source/_vanilla/original), including vessel variants, aircraft loadouts and Pacific Strike's trigger examples, and the [archived developer field guide](https://github.com/mikprin/sea_power_editor/blob/main/docs/examples_from_dev/MissionFileInformation.ini). These mirrors are compatibility references; installed game files remain authoritative. No third-party unit assets are redistributed.

See [TESTING.md](TESTING.md) for the acceptance checklist before calling this campaign playable or balanced.
