from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:
    def __init__(self):
        # small + fast + accurate
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def embed(self, text: str):
        try:
            vec = self.model.encode(text)
            return vec.tolist()
        except Exception as e:
            print("Embedding error:", e)
            return [0.0] * 384
