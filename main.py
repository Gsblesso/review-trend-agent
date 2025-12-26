from agent import fetch_reviews
from topic_agent import TopicAgent
from trend_builder import build_trend

APP_ID = "in.swiggy.android"

def main():
    print("Fetching reviews from Google Play Store...")
    df = fetch_reviews(APP_ID, count=1500)

    print("Assigning topics using Agentic AI...")
    agent = TopicAgent()
    df["topic"] = df["content"].apply(agent.assign_topic)

    print("Building trend analysis table...")
    trend_df = build_trend(df)

    trend_df.to_csv("output/trend_report.csv")
    print("Trend report generated at output/trend_report.csv")

if __name__ == "__main__":
    main()
