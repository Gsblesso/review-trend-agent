import pandas as pd
from collections import defaultdict

def build_trend(df):
    trend = defaultdict(lambda: defaultdict(int))

    for _, row in df.iterrows():
        topic = row["topic"]
        date = row["date"]
        trend[topic][date] += 1

    trend_df = pd.DataFrame(trend).fillna(0).T
    trend_df = trend_df.sort_index(axis=1)

    return trend_df
