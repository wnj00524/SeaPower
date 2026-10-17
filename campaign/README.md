# Operation Broken Trident — Sea Power Task Force Mode

**Status: structured alpha package, statically checked; NOT game-tested.**

Fictional Cold War campaign using period-era base-game units. US Sixth Fleet versus the Soviet Fifth Operational Squadron, 8 September–1 October 1985. Twelve authored mission `.ini` files and Task Force Mode campaign files. No external unit mod is intended to be required.

## Installation

1. Close Sea Power. Locate its `Sea Power_Data/StreamingAssets` directory.
2. Copy the enclosed `user/Operation_Broken_Trident` folder into `StreamingAssets/user/Operation_Broken_Trident` (merge if needed). The result must contain `.../user/Operation_Broken_Trident/_info.ini`.
3. Relaunch Sea Power, ensure the mod is enabled in Mod Manager, open Campaigns, and find **Operation Broken Trident (NATO - Task Force Mode)**.
4. Start **Supported** difficulty for first test, allocate at least two ships, and launch mission 1.
5. Do not touch `StreamingAssets/original`. If any campaign does not appear, check the game log and compare the user's copy against the current built-in `original/campaigns/pacific-strike-task-force` format.

## What's included

- `campaign.ini`: campaign structure, unlock chain, persistent fleet rules, difficulty presets and points.
- `player_task_force_roster.ini`: period US Navy vessel and land-based aircraft choices, with campaign-specific prices.
- `commander_settings.ini`: minimal US Navy commander ranks with built-in image paths.
- `missions/`: twelve authored playable-shape scenarios with task-force anchor, opponents, objectives, and time / success / failure triggers.
- `CAMPAIGN_DESIGN.md`: narrative, missions, logistics and realism constraints.
- `TESTING.md`: staged in-game QA checklist.
- `BRIEFINGS.md`: illustrated orders, chart conventions, art provenance and regeneration instructions.

## Important alpha limitations

This prototype's battle resolution uses objective triggers against fixed enemies, area arrival, or survival for a defined window. It has **not** been run inside Sea Power. Aircraft AI, task-force spawn behaviour, campaign unlocks, neutral AI and weapon-state persistence require live verification. Fixed Soviet bomber flights remain opponents; player Task Force Builder now also offers P-3C, F-15C, F-4E, EA-6B and A-6E aircraft for mission airbases. Carrier strike aircraft are provided as hypothetical shore-based detachments, not as a player-purchasable aircraft carrier. There is **no dynamic war**, strategic enemy resource model, campaign branching or conditional carry-over of enemy damage beyond the game's own supported Task Force persistence. 'Relief' / 'convoy' ship routing in scenarios is intentionally simple and needs editor inspection for geography, depth, AI paths and duration.

The unmodded unit IDs and many NATO variants were cross-checked against the built-in Pacific Strike campaign and publicly archived Sea Power original unit files. Exact compatibility depends on installed game version. ApproximateVersion is set to 0.8.0; check the latest game release.

## References

- Developer Task Force Mode campaign authoring guide: https://steamcommunity.com/sharedfiles/filedetails/?id=3756769210
- Community mission trigger guide: https://steamcommunity.com/sharedfiles/filedetails/?id=3756786658
- Vanilla Pacific Strike file layout: `original/campaigns/pacific-strike-task-force/` in your Sea Power installation.

## Land-based Task Force aircraft (airbase revision)

Every mission now contains **one player-side NATO airbase** with `CustomAirGroup=True` (no free default aircraft). The campaign enables **Airbase Prep** on every mission, providing four ready aircraft-group slots and eight in-progress slots. Buy eligible aircraft through Task Force Builder and assign/prep them using **Prepare Airbase** before launching a mission. Aircraft not pre-staged may require preparation after the mission begins. Ship-assigned helicopters remain with their ships; they are not automatically deployed to shore bases.

The airfields use the generic original-game `nato_small_airbase` model, renamed and positioned at real-world bases. A map/terrain check and verification of runway/flight-deck aircraft compatibility in Sea Power is still required. Aircraft land on the airbase represented in the mission; no additional Workshop aircraft or airfield mods are intended.

| Missions | Friendly airbase |
|---|---|
| 01–03 | NAS Sigonella, Sicily |
| 04–06 | Souda Bay Air Base, Crete |
| 07 | RAF Akrotiri, Cyprus (fictional US access) |
| 08–12 | Souda Bay Air Base, Crete |

## Reinforced scenario revision

See `SCENARIO_REVIEW.md` for per-mission force totals, geography findings, AI settings and remaining in-game checks. All 12 missions now contain independent merchant/fishing traffic and shore defences. Enemy airborne flights are explicitly authored; four additional MiG-23MLDs at each enemy base are reserves whose AI launch behaviour requires in-game verification. Friendly airbases use explicit `GeoPosition` coordinates. The increased opposition has not been balanced in game; start on Supported and preserve fighter and SAM ammunition.
