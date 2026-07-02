from app.services.retrieval_service import RetrievalService
from app.services.llm_service import LLMService


class RecommendationService:

    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.llm_service = LLMService()

    def recommend(
        self,
        requirements,
        search_query: str,
    ):

        recommendations = self.retrieval_service.retrieve(
            search_query
        )

        reply = self.llm_service.generate_recommendation(
            requirements=requirements.model_dump(),
            recommendations=recommendations,
        )

        if reply is None:

            reply = (
                "Gemini is unavailable.\n\n"
                "Showing semantic search results."
            )

        return reply, recommendations