from shapely.geometry import MultiPolygon
from app.transformers.pdok_transformer import transform_features
polygon = {
    "type": "Polygon",
    "coordinates": [[
        [155000, 463000],
        [155100, 463000],
        [155100, 463100],
        [155000, 463000],
    ]],
}
data = {
    "features": [{
        "id": "NL-1",
        "properties": {},
        "geometry": polygon,
    }]
}
gdf = transform_features(data)
assert len(gdf) == 1
assert isinstance(gdf.geometry.iloc[0], MultiPolygon)
assert gdf.crs.to_epsg() == 4326
assert gdf.iloc[0]["country_code"] == "NL"
empty = transform_features({
    "features": [{
        "id": "NL-2",
        "properties": {},
        "geometry": None,
    }]
})
assert empty.empty
print("PDOK checks passed")