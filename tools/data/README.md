# Coastline reference

`mediterranean-land.geojson` is Natural Earth's public-domain 1:50m land data, clipped to 10–38°E and 29–39°N. Source blob: `c412c52b5286ba727dcb7047ecd6080bcbeb8298` in https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_land.geojson.

Natural Earth terms: https://www.naturalearthdata.com/about/terms-of-use/.

This approximate coastline includes Malta/Gozo and Mediterranean islands. It contains no bathymetry or Sea Power terrain. A 3 NM clearance check catches authored coastal crossings; it cannot certify water depth, engine steering, formation spacing or actual game terrain. Do not use it for real navigation. The validator supports only this regional campaign.

`falklands-land.geojson` contains whole Natural Earth 1:50m polygons with an exterior vertex within 66–47°W, 56–45°S, including the Falklands and adjacent South American coast. Source: the same `ne_50m_land.geojson` linked above, retrieved 18 October 2026. Whole intersecting polygons are retained so clipping introduces no false coastline edges. This data is used only by `validate_falklands.py`; it supplies no bathymetry or engine terrain guarantee.
