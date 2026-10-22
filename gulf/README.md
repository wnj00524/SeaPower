# Operation Desert Lantern — Sea Power Task Force Mode

Eight-mission fictional Gulf campaign. Strike Iranian coastal missile, radar, drone-control and air-defence sites while protecting commercial shipping from missile, drone, submarine and aircraft threats. It uses stock unit prefabs, with Soviet-origin equipment IDs serving as Iranian equipment proxies. This is a fictional game scenario, not a description of current operations.

## Install

Copy `user/Operation_Desert_Lantern` into Sea Power’s `Sea Power_Data/StreamingAssets/user/` directory, enable it in Mod Manager, then select **Operation Desert Lantern (Task Force Mode)** in Campaigns. The Easy preset starts with **100,000 points**. Every mission includes a player airbase at RAFO Masirah and Airbase Prep with four ready and eight in-progress group slots.

The eight missions provide eight Iranian land units apiece, layered with surface, submarine, aircraft and civilian traffic. The land sites are optional tactical targets; the mission’s primary victory triggers remain tied to its designated surface threat. Rearm and repair availability varies by mission.

## Terrain and status

Land units and the player airbase use zero-altitude `GeoPosition` coordinates selected for known land locations on Iran’s southern coast and Masirah Island. This repository has no Sea Power terrain/elevation tiles for the Gulf, and the package has not been loaded in the game. The static check verifies coordinate ranges and zero-altitude land placements, but cannot certify that every prefab’s footprint clears local terrain. Inspect all eight maps in the Sea Power Mission Editor and adjust any prefab that intersects terrain before treating the campaign as game-tested. Sea routes, depths, airbase aircraft compatibility and AI behavior also require in-game acceptance.

Run `python tools/validate_desert_lantern.py` for structural checks.
