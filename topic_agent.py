from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class TopicAgent:
    def __init__(self, similarity_threshold=0.82):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.topics = []
        self.embeddings = []
        self.threshold = similarity_threshold

    def assign_topic(self, text):
        embedding = self.model.encode([text])[0]

        if not self.topics:
            self.topics.append(text)
            self.embeddings.append(embedding)
            return text

        similarities = cosine_similarity(
            [embedding],
            self.embeddings
        )[0]

        best_match_idx = np.argmax(similarities)

        if similarities[best_match_idx] >= self.threshold:
            return self.topics[best_match_idx]
        else:
            self.topics.append(text)
            self.embeddings.append(embedding)
            return text
