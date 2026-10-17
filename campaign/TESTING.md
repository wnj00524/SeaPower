# Sea Power integration test checklist (in-game only)

The zip has been statically validated but **not launched in Sea Power**. Run these before sharing as playable:

- [ ] Campaign appears in Campaigns when enabled, without errors in log.
- [ ] Starting points, difficulty selection, unit roster and available vessel variants load.
- [ ] Buy 2 vessels. Mission 1 generates the actual purchased units, not the anchor Spruance.
- [ ] Both 1st and 2nd purchased ships spawn afloat, near convoy, in valid deep water.
- [ ] AI convoy moves toward waypoint without grounding, and the success trigger fires on area entry.
- [ ] Neutral destroyed trigger marks defeat and the campaign saves expected outcome.
- [ ] Mission end occurs after trigger delay; mission 2 unlocks on acceptable victory.
- [ ] Destroying a marked opponent triggers objective completion for mission 2 (ASW) and mission 5 (surface).
- [ ] Mission 6 survival trigger fires at 4500 seconds before its time limit.
- [ ] Submarine and Tu-16K aircraft spawn and fight (verify loadouts / flight altitude / routes).
- [ ] Destroyed ships do not reappear in Task Force Builder; surviving ships retain correct damage / ammunition.
- [ ] Rearm=False and Repair=False meaningfully restrict player maintenance where specified.
- [ ] Campaign-specific roster purchase restrictions work, later missions unlock heavier cruisers.
- [ ] All 12 missions succeed/fail and unlock correct subsequent mission.
- [ ] Mission 12 sets end of campaign / service record correctly.
- [ ] Mod tested on clean Sea Power version >= 0.8.0 with unit mods disabled.

If a trigger fails: compare the mission's corresponding block against a current built-in scenario or import/resave the scenario in the game's mission editor. Check whether neutrals are targeted by enemy AI; if they are ignored, use a friendly scripted objective vessel instead and revise the generated anchor setup accordingly.

## Land-based aviation regression checklist (all 12 missions)

- [ ] Task Force Builder offers P-3C, F-15C, F-4E, EA-6B and A-6E before each mission (when points permit).
- [ ] Player-side `nato_small_airbase` spawns on land, at the listed geographic airfield, with the correct NATO alignment and name.
- [ ] No stock/default free aircraft appear at the base before buying aircraft.
- [ ] **Prepare Airbase** is offered before each mission; 4 ready and 8 in-progress aircraft-group slots appear.
- [ ] Buy at least one P-3C and one fighter. They can be assigned to the airbase, readied and launched.
- [ ] Land-based aircraft can take off, fly to the mission operating area and recover at their airbase without terrain collision or compatibility errors.
- [ ] Exercise an A-6E strike mission and an EA-6B ECM mission from a shore base; check loadouts and ammunition availability.
- [ ] Check aircraft losses, inventories and preparation states after transitioning between missions; no duplication / free regeneration.
- [ ] Verify base damage/closure effects do not trap aircraft without alternate recovery options.
- [ ] Mission 1 (Sigonella), 4 (Souda) and 7 (Akrotiri) are representative early checks, then smoke-test missions 2–12.
- [ ] If airbase models intersect the ground or appear offshore, adjust `RelativePositionInNM` in the Mission Editor / F10 and resave.
- [ ] If any aircraft cannot be allocated, inspect actual aircraft squadrons and base aircraft-capacity compatibility in the installed version.

## Reinforced revision acceptance (all 12 missions)

- [ ] Inspect every surface/submarine spawn and route in the engine, including water depth for `belowlayer`; static coastline clearance alone does not establish safe depth.
- [ ] Confirm positive-north waypoint Z convention and mission 1 convoy exit south of Malta. Check purchased-fleet placement around its anchor.
- [ ] Verify corrected geographic positions of Sigonella, Souda and Akrotiri and all enemy land units on game terrain.
- [ ] Check MiG-23MLD, Tu-16K and Tu-22M2 loadouts in the installed stock catalog; confirm finite-fuel flights engage and do not simply overfly the task group.
- [ ] Observe radar-silent attackers, emitting escorts, fighter interception and submarine contacts with enemy AI enabled. Confirm Tight does not leave combatants indefinitely passive and Free does not cause unintended neutral attacks.
- [ ] Observe independent fighter and bomber routes from both bearings. Do not assume coordinated attacks or timed waves merely from route spacing.
- [ ] Inspect each enemy base's four reserve fighters. Record whether native flight-deck AI launches them; airborne opposition must still work if it does not.
- [ ] Inspect SA-5/SA-3 engagement and fire-control behaviour, coastal launcher targeting and P-14 detection. Check actual shore coverage before claiming a threat in the central offshore battle area.
- [ ] Verify three extra neutral freighter/fishing contacts per mission, differing radar state and traffic directions; preserve protected NeutralVessel1 loss and escort-arrival triggers.
- [ ] Play the entire Supported campaign, including no-rearm legs, before tuning Standard/Severe. Confirm aircraft/ship losses and ammunition expenditure allow progress without requiring destruction of new optional land targets.
- [ ] Confirm campaign menu air/land threat indicators reflect the new scenario forces.

## Illustrated briefing acceptance

- [ ] Open all twelve briefings: confirm the English text panel scrolls, wraps and displays its phase illustration.
- [ ] Confirm each right pane displays its own mission title, theatre context, correct friendly airbase and local task chart.
- [ ] Check the actual Noesis renderer at the intended game resolution and UI scale. Static XML parsing is not a rendering test.
- [ ] Compare the escort safety circles against the tactical map in missions 1, 3, 7, 8 and 11. Check that other task rings are understood as illustrative.
- [ ] Check mission 6 states survival for 75 minutes, mission 9 requires the Slava and Krivak, and mission 10 requires Udaloy/Kara/Krivak.
- [ ] Check mission 11's text agrees with its eastbound route and that start/victory/defeat messages use the new mission-specific wording.
- [ ] Confirm no exact hostile spawn positions or unearned friendly aircraft are revealed or promised by the briefing.
