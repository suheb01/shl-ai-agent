from app.retriever.loader import load_catalog
from app.retriever.embeddings import EmbeddingModel
from app.retriever.vector_store import collection


embedding_model = EmbeddingModel()


def build_index():
    """
    Build the ChromaDB vector index from the SHL assessment catalog.
    """

    catalog = load_catalog()

    print(f"Loaded {len(catalog)} assessments.")

    for assessment in catalog:

        # Create a rich searchable document
        document = f"""
Assessment Name: {assessment.get("name", "")}

Description:
{assessment.get("description", "")}

Job Levels:
{", ".join(assessment.get("job_levels", []))}

Languages:
{", ".join(assessment.get("languages", []))}

Duration:
{assessment.get("duration", "")}

Remote:
{assessment.get("remote", "")}

Adaptive:
{assessment.get("adaptive", "")}

Keywords:
{", ".join(assessment.get("keys", []))}
"""

        # Generate embedding
        embedding = embedding_model.encode(document)

        # Store in ChromaDB
        collection.add(
            ids=[str(assessment["entity_id"])],
            documents=[document],
            embeddings=[embedding],
            metadatas=[
                {
                    "name": assessment.get("name", ""),
                    "link": assessment.get("link", ""),
                    "duration": assessment.get("duration", ""),
                    "job_levels": ", ".join(
                        assessment.get("job_levels", [])
                    ),
                    "languages": ", ".join(
                        assessment.get("languages", [])
                    ),
                    "remote": str(assessment.get("remote", "")),
                    "adaptive": str(assessment.get("adaptive", "")),
                }
            ],
        )

    print("✅ Vector database created successfully!")


if __name__ == "__main__":
    build_index()