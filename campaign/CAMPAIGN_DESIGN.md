# Operation Broken Trident — Campaign Design

## Premise

The Mediterranean in September 1985 has become the most confined front of a much wider fictional NATO–Soviet crisis. Tensions between the U.S. Sixth Fleet and the Soviet Fifth Operational Squadron grow in the weeks following a disputed clash south of Crete. Command has not issued a licence for indiscriminate engagement: Cyprus, Malta and major shipping lanes remain populated by neutrals, and a tactical success that kills civilians can be a strategic defeat.

The player commands US Navy surface combatants and can purchase a small land-based NATO air detachment, using allied airfields for preparation, launch and recovery. Ships retain damage and ammunition state between sorties, with scarce rearm and repair opportunities. Political context is alternative history; dates and place names are illustrative rather than claims about real battles.

## Gameplay constraints

- No additional ship/unit mods intended. U.S. Navy purchase roster comes from public 1985-era Pacific Strike variants.
- Ship survival, stored ammunition, repairs and new purchases use native Task Force Mode.
- Difficulty changes starting requisition points; prices are game-balance abstractions.
- No requirement to sink every enemy ship in escort, ASW or survival missions.
- No attacks on neutral ports, neutral shipping or civilian infrastructure are campaign objectives.
- Soviet forces are already present in the Mediterranean at outbreak; the scenario does not presume wartime reinforcement through the Turkish Straits.
- No campaign branches or global enemy campaign simulation are implemented.

## Operational phases

### Phase I — The fuse: shadowing, convoy escort and submarine hunts
**01. Sicilian Passage** (8 Sep 1985, centre 35.45°N 14.2°E) — Escort M/V Sea Amber through the southern approaches to Malta while an unidentified missile craft group tests the new rules of engagement.
Mission condition: escort. Rearm: yes; repair: yes; completion points: 28.
**02. Broken Contact** (9 Sep 1985, centre 35.05°N 17.65°E) — Find and neutralise a Soviet Foxtrot reported inside the convoy approach to the Ionian Sea.
Mission condition: asw. Rearm: no; repair: no; completion points: 32.
**03. The Narrows** (11 Sep 1985, centre 36.1°N 15.45°E) — Push an urgent logistics freighter through the Sicily Channel in spite of Soviet patrol craft.
Mission condition: escort. Rearm: yes; repair: yes; completion points: 30.
**04. Crete Barrier** (13 Sep 1985, centre 34.6°N 24.75°E) — Sweep an ASW barrier south of Crete for an incoming Soviet diesel-electric submarine.
Mission condition: asw. Rearm: no; repair: no; completion points: 36.

### Phase II — The fire: increasingly dangerous missile engagements and strained replenishment
**05. The Black Sea Squadron** (15 Sep 1985, centre 34.3°N 26.85°E) — Intercept a Soviet surface detachment gathering south-east of Crete before it can screen a long-range raid.
Mission condition: attack. Rearm: yes; repair: yes; completion points: 42.
**06. Steel Rain** (17 Sep 1985, centre 33.9°N 23.15°E) — Hold a radar picket south of Crete through a coordinated Soviet bomber and missile-ship attack.
Mission condition: survive. Rearm: no; repair: no; completion points: 42.
**07. Lifeline to Cyprus** (20 Sep 1985, centre 33.3°N 31.0°E) — Protect a relief freighter travelling into the Cyprus approaches while Soviet surface forces attempt to establish a blockade.
Mission condition: escort. Rearm: yes; repair: yes; completion points: 45.
**08. Guard the Oiler** (22 Sep 1985, centre 34.5°N 21.0°E) — Cover an underway-replenishment rendezvous while Soviet surface units seek the support ship.
Mission condition: escort. Rearm: yes; repair: yes; completion points: 45.

### Phase III — The line: cruiser engagements, evacuation and conditional ceasefire
**09. Sunken Spear** (25 Sep 1985, centre 34.55°N 27.1°E) — Destroy a Soviet missile cruiser operating as the forward command ship in the eastern Mediterranean.
Mission condition: attack. Rearm: no; repair: no; completion points: 50.
**10. Iron Ring** (27 Sep 1985, centre 33.85°N 25.65°E) — Break an integrated Soviet cruiser and destroyer screen between Crete and the Levant.
Mission condition: attack. Rearm: yes; repair: yes; completion points: 55.
**11. Outbound** (29 Sep 1985, centre 35.05°N 20.0°E) — Escort an evacuation transport west across the Ionian Sea, keeping the task force intact under pressure.
Mission condition: escort. Rearm: no; repair: no; completion points: 42.
**12. Broken Trident** (1 Oct 1985, centre 34.2°N 23.8°E) — Confront the last major Soviet surface strike group south of Crete and end the Mediterranean naval offensive.
Mission condition: attack. Rearm: no; repair: no; completion points: 0.

## Historical and realism notes

- The actual Soviet Fifth Operational Squadron maintained a permanent Mediterranean naval presence; this is a fictional shooting war, not a historical account.
- US vessels are selected from 1985-compatible game classes, not a claim that particular hulls were on a specific deployment.
- Slava, Kara, Kashin, Krivak, Nanuchka, Foxtrot, Kilo and Tu-16K are representative Soviet platforms available in the base-game catalog; verify each selected ship variant and aeroplane service dates in the actual installed unit files.
- NATO ability to field heavy cruisers and replacement ships is expressed as requisition points, not instantaneous real-world teleportation.
- The reinforced revision assumes fictional Soviet expeditionary basing permission in Libya and, for mission 7, Syria. The host states are not separate playable factions. Chinese-designed coastal missiles under Soviet control are a fictional expeditionary equipment choice.

## Expansion options after alpha testing

1. Replace simple escort triggers with multi-stage area and warning rules.
2. Add optional airborne Air Tasking slots in addition to the shore-based Airbase Prep now provided in every mission.
3. Model convoy protection as friendly allied units if neutral AI proves passive.
4. Create mission briefings and campaign art.
5. Add political fail states for neutral deaths, independent of operation completion.
6. Validate map extents, coastlines, bathymetry and exact flight/ship AI behaviour in the mission editor.

## NATO airbases and aviation support

Airbase assignment: missions 1–3 NAS Sigonella; missions 4–6 Souda Bay; mission 7 RAF Akrotiri; missions 8–12 Souda Bay. Airfields are placed near their real geographic runway coordinates as player land units using the original-game `nato_small_airbase` prefab and empty custom air groups. A player may purchase P-3C, F-15C, F-4E, EA-6B and A-6E aircraft; Task Force Mode Airbase Prep is offered in all twelve missions. Shore deployments of carrier-capable naval aircraft are a fictional wartime expedient. USAF aircraft are hypothetical NATO detachments. US use of RAF Akrotiri is likewise a fictional allied-access arrangement. Airbase preparation is not the same as airborne Air Tasking; no pre-airborne slots are authored at this stage.
