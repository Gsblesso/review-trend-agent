from google_play_scraper import reviews
import pandas as pd

def fetch_reviews(app_id, count=1000):
    result, _ = reviews(
        app_id,
        lang="en",
        country="in",
        count=count
    )

    rows = []
    for r in result:
        rows.append({
            "date": r["at"].date(),
            "content": r["content"]
        })

    return pd.DataFrame(rows)
