# Sea Power Task Force Campaigns

## Operation Southern Resolve — Falklands 1988

Eight-mission alternate-history campaign: Argentina invades the Falklands with Cuban and Venezuelan backing. Command a US reinforcement group in the British-led response. Persistent fleet, evacuation and replenishment escorts, ASW, air defence and military supply interdiction. Uses stock units with documented equipment proxies. **Structured alpha; not game-tested.**

Download `Operation_Southern_Resolve_Sea_Power_Alpha.zip` and follow [installation, mission list and limitations](falklands/README.md). Source: `falklands/`. See [in-game acceptance checks](falklands/TESTING.md).

```sh
python tools/validate_falklands.py
python tools/build_falklands_package.py --check
```

## Operation Broken Trident — Mediterranean 1985


Twelve-mission fictional Cold War Mediterranean Task Force campaign.

Download `Operation_Broken_Trident_Sea_Power_Alpha_Airbases.zip`, extract it, then follow [installation instructions](campaign/README.md). Replace the previous mod folder so old files do not linger. The archive contains the reinforced revision.

The editable source is in `campaign/`. See [scenario review](campaign/SCENARIO_REVIEW.md) for force changes, geography findings and limitations, and [in-game checks](campaign/TESTING.md) before treating it as a tested campaign.

From the repository root, using Python 3 with no additional packages:

```sh
python tools/validate_scenarios.py
python tools/build_package.py
python tools/build_package.py --check
```

Static coastline/structure checks pass; this revision has **not been played in Sea Power**.

All twelve missions now include [illustrated narrative briefings](campaign/BRIEFINGS.md), with three original campaign paintings, twelve tactical charts and mission-specific dispatches and debriefs. Run `python tools/validate_briefings.py` to check briefing links and assets.
