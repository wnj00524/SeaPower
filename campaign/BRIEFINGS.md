# Illustrated mission briefings

All twelve missions have English briefing panels using Sea Power's XAML briefing system. The left pane contains a campaign illustration and scrollable orders. The right pane contains that mission's theatre and local planning chart. The in-mission dispatch and victory/failure messages also have mission-specific narrative.

## What the player receives

- A connected fictional crisis, from uncertain convoy passages through sustained naval/air combat to evacuation cover and a final strike-group engagement.
- A commander dispatch, situation, explicit completion conditions, qualified intelligence, execution guidance, ROE, aviation/sustainment and date/weather.
- Mission-specific charts built from the bundled Natural Earth coastline. Friendly airbases and operating areas are shown. Escort routes and safety areas come directly from mission data. Other task rings are illustrative orientation symbols, not new scripted constraints. Exact enemy ship, aircraft and submarine positions are deliberately omitted.
- Three original AI-generated phase illustrations, reused across four missions each: **The Fuse**, **The Fire**, **The Line**. These are fictional atmosphere, not historical photographs, reconnaissance or reliable technical recognition plates.

The orders do not promise aircraft the player has not bought or prepared. Mission 6 states its actual 75-minute survival condition and does not imply a spawned relief force. Mission 9 identifies both required targets. Mission 10 names Udaloy/Kara/Krivak, rather than incorrectly implying a cruiser. Mission 11 describes the existing eastbound escort route. These are text corrections; this revision does not change the forces, routes, triggers or scoring mechanics from the reinforced scenario revision.

## Files and rebuilding

Editable narrative source: `briefing_source/missions.json` at repository root. Mission-specific `Orders_en.md` files sit beside the XAML panels for easy reading. Game-facing panels are explicitly linked from each mission's `Language_en` block. All imagery is in `campaign/user/Operation_Broken_Trident/campaigns/operation-broken-trident/briefing_assets`.

To regenerate panels, narrative messages and charts, install Pillow in your development environment, then run `python tools/build_briefings.py`. The committed images mean players and normal CI do not require Pillow or an image-generation account. To validate: `python tools/validate_briefings.py`. Then rebuild the installable ZIP with `python tools/build_package.py` and verify with `--check`.

The validator parses all 24 XML panels, resolves their game-relative paths and image bindings, checks the 12 mission/phase assignments, and validates PNG chunk CRCs, complete decompression and dimensions divisible by four. Local QA additionally decodes every JPEG and PNG with Pillow. Coastline and structural scenario checks remain separate.

## Image provenance and permitted use

The three phase illustrations were created for this repository on 17 October 2026 with ChatGPT's built-in image-generation tool. No third-party stock photography, scraped images or borrowed game artwork is included. Prompts are retained in `briefing_source/ART_PROMPTS.md`. Treat the illustrations as AI-generated fictional campaign artwork, subject to the applicable OpenAI output terms; no claim of historical authenticity or exclusive copyright is made.

Tactical charts were drawn by code using the public-domain Natural Earth coastline already documented in `tools/data/README.md`. They are original planning graphics, not official charts or navigation products.

## Runtime verification still required

The XML schema, `Assets[stem]` bindings and mission keys follow [an authored Sea Power tutorial example](https://github.com/rangerzero003/sea-power/blob/main/missions/Tutorial%20Missions/Basic%20Surface%20Warship%20Maneouvers.ini) and its briefing panels. Static XML parsing cannot establish Noesis rendering compatibility. In Sea Power, open all twelve briefings and check scrolling, wrapping, image loading, English fallback, chart readability and start/end messages before declaring this game-tested. At a minimum inspect missions 1, 6, 7, 9, 11 and 12 for the different objective and airbase cases.
