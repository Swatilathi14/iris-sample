import os
from app.loaders.pdok_loader import load_cadastre
from app.scrapers.pdok.pdok_scraper import PdokScraper
from app.transformers.pdok_transformer import transform_features

def run():
  url = os.environ["PDOK_WFS_URL"]
  feature_type = os.environ["PDOK_FEATURE_TYPE"]
  
  data = PdokScrape(url, feature_type).fetch_all()
  gdf = transform_features(data)
  loaded = load_cadastre(gdf)

  print(f"Fetched: {len(data['feature'])}")
  print(f"Loaded: {loaded}")

if __name__ == "__main__":
  run