# Operation Broken Trident — Sea Power

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
