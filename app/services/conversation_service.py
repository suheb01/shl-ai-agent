from app.agent.conversation import ConversationManager
from app.agent.requirements import RequirementExtractor

from app.models.schemas import (
    ChatRequest,
    ChatResponse,
    Recommendation,
)

from app.services.recommendation_service import RecommendationService


class ConversationService:
    """
    Handles the overall conversation workflow.

    Responsibilities:
    1. Extract recruiter requirements.
    2. Determine if clarification is needed.
    3. Build the search query.
    4. Delegate recommendation generation.
    5. Return the final response.
    """

    def __init__(self):
        self.requirement_extractor = RequirementExtractor()
        self.conversation_manager = ConversationManager()
        self.recommendation_service = RecommendationService()

    def chat(self, request: ChatRequest) -> ChatResponse:

        # ----------------------------------------------------
        # Step 1 : Extract recruiter requirements
        # ----------------------------------------------------
        requirements = self.requirement_extractor.extract(
            request.messages
        )

        print("\n========== Extracted Requirements ==========")
        print(requirements.model_dump())

        # ----------------------------------------------------
        # Step 2 : Ask clarification if required
        # ----------------------------------------------------
        if self.conversation_manager.needs_clarification(
            request.messages
        ):

            return ChatResponse(
                reply=self.conversation_manager.clarification_question(),
                recommendations=[],
                end_of_conversation=False,
            )

        # ----------------------------------------------------
        # Step 3 : Build search query
        # ----------------------------------------------------
        search_query = requirements.role or ""

        if requirements.seniority:
            search_query += f" {requirements.seniority}"

        if requirements.experience:
            search_query += f" {requirements.experience}"

        print("\n========== Search Query ==========")
        print(search_query)

        # ----------------------------------------------------
        # Step 4 : Get recommendations
        # ----------------------------------------------------
        reply, results = self.recommendation_service.recommend(
            requirements=requirements,
            search_query=search_query,
        )

        print("\n========== Final Recommendations ==========")
        print(results)

        # ----------------------------------------------------
        # Step 5 : Convert dictionaries to Recommendation model
        # ----------------------------------------------------
        recommendations = [
            Recommendation(**item)
            for item in results
        ]

        # ----------------------------------------------------
        # Step 6 : Return API response
        # ----------------------------------------------------
        return ChatResponse(
            reply=reply,
            recommendations=recommendations,
            end_of_conversation=False,
        )