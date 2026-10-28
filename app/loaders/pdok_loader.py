from app.database.session import engine

SCHEMA = "iris_staging"
TABLE = "cadastre_netherlands"

DATABASE_URL = str(engine.url).lower()

if "iris_core" in DATABASE_URL:
  raise RuntimeError("iris_core database is not allowed")

def load_cadastre(gdf):
  if SCHEMA != "iris_staging":
    raise RuntimeError("Only iris_staging is allowed")
 
  if gdf.empty:
    return 0

  gdf = gdf.drop_duplicates(subset="source_id")

  with engin.begin() as conn:
    existing = set(
      conn.exec_driver_sql(f"SELECT source_id FROM {SCHEMA}.{TABLE}").scalars()
    )
  
  gdf = gdf[~gdf["source_id"].isin(existing)]

  if gdf.empty:
    return 0

  gdf.to_postgis(TABLE,
                 engine,
		 schema=SCHEMA,
		 if_exists="append",
		 index=False)
  return len(gdf)