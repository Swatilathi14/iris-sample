import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon, shape

def transform_features(data, source_crs= "EPSG:28992", target_crs="EPSG:4326"):
  rows = []
  
  for features in data.get("features", []):
    geometry = features.get("geometry")
    properties = features.get("properties", {})
    source_id = features.get("id")
    if not source_id:
      continue
    
    if not geometry:
      continue
    
    geom = shape(geometry)

    if geom.is_empty or not geom.is_valid:
      continue 

    if isinstance(geom, Polygon):
      geom= MultiPolygon([geom])

    if not isinstance(geom, MultiPolygon):
      continue

    rows.append({**properties, "source_id": source_id, "country_code": "NL", "geometry": geom, })
 
  if not rows:
    return gpd.GeoDataFrame(columns=["geometry"], geometry="geometry")

  gdf = gpd.GeoDataFrame(rows,geometry="geometry", crs=source_crs)
  return gdf.to_crs(target_crs)