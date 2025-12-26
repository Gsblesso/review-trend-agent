# Review Trend Analysis Agent (Agentic AI)

An Agentic AI system that analyzes Google Play Store reviews and generates
a 30-day rolling trend analysis of customer issues, requests, and feedback.

This project is designed for product and analytics teams to identify
recurring and emerging user pain points at scale.

---

## 🚀 Key Features

- **Agentic Topic Discovery**
  - Uses semantic embeddings instead of traditional topic modeling (LDA/LDA-like approaches)
  - Automatically merges similar feedback into a single evolving topic

- **High Recall Trend Analysis**
  - Prevents topic fragmentation (e.g., “delivery guy rude” vs “delivery partner behaved badly”)
  - Ensures accurate trend signals over time

- **Daily Batch Processing**
  - Simulates real-world ingestion of reviews on a day-by-day basis

- **Clean Tabular Output**
  - Rows: Topics
  - Columns: Dates (T-30 → T)
  - Values: Frequency of topic occurrence

---

## 🧠 Architecture Overview

1. Fetch reviews from Google Play Store
2. Assign topics using an Agentic AI (semantic similarity + memory)
3. Aggregate topic frequencies per day
4. Generate a trend table consumable by product teams

---

## 🛠️ Tech Stack

- Python
- SentenceTransformers
- Scikit-learn
- Pandas
- Google Play Scraper

---

## 📂 Project Structure

