from shapely.geometry import MultiPolygon
from app.transformers.pdok_transformer import transform_features

def feature(geometry, source_id="NL-1"):
    return {
        "id": source_id,
        "properties": {},
        "geometry": geometry,
    }

def test_polygon_becomes_multipolygon():
    polygon = {
        "type": "Polygon",
        "coordinates": [[[155000, 463000], [155100, 463000],
                         [155100, 463100], [155000, 463000]]],
    }
    gdf = transform_features({"features": [feature(polygon)]})
    assert len(gdf) == 1
    assert isinstance(gdf.geometry.iloc[0], MultiPolygon)
    assert gdf.crs.to_epsg() == 4326
    assert gdf.iloc[0]["country_code"] == "NL"

def test_missing_geometry_is_skipped():

    gdf = transform_features({"features": [feature(None)]})
    assert gdf.empty

def test_duplicate_source_id_can_be_identified():
    polygon = {
        "type": "Polygon",
        "coordinates": [[[155000, 463000], [155100, 463000],
                         [155100, 463100], [155000, 463000]]],
    }
    gdf = transform_features({
        "features": [feature(polygon), feature(polygon)]
    })
    assert gdf["source_id"].duplicated().sum() == 1