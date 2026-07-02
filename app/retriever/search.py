from app.retriever.embeddings import EmbeddingModel
from app.retriever.vector_store import collection


class Retriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()

    def search(self, query: str, top_k: int = 5):

        query_embedding = self.embedding_model.encode(query)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        recommendations = []

        ids = results.get("ids", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for i in range(len(ids)):

            recommendations.append(
                {
                    "id": ids[i],
                    "name": metadatas[i]["name"],
                    "url": metadatas[i]["link"],
                    "duration": metadatas[i]["duration"],
                    "job_levels": metadatas[i]["job_levels"],
                    "languages": metadatas[i]["languages"],
                    "remote": metadatas[i]["remote"],
                    "adaptive": metadatas[i]["adaptive"],
                    "score": round(1 - distances[i], 4)
                }
            )

        return recommendations