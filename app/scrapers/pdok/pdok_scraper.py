import requests
class PdokScraper:
    def __init__(self, url, feature_type, page_size=1000):
        self.url = url
        self.feature_type = feature_type
        self.page_size = page_size
    def fetch_page(self, start_index=0):
        params = {
            "service": "WFS",
            "version": "2.0.0",
            "request": "GetFeature",
            "typeNames": self.feature_type,
            "outputFormat": "application/json",
            "count": self.page_size,
            "startIndex": start_index,
        }
        response = requests.get(self.url, params=params, timeout=60)
        response.raise_for_status()
        return response.json()
    def fetch_all(self):
        features = []
        start = 0
        while True:
            page = self.fetch_page(start)
            batch = page.get("features", [])
            features.extend(batch)
            if len(batch) < self.page_size:
                break
            start += self.page_size
        return {"type": "FeatureCollection", "features": features}