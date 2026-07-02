from typing import List

from app.models.schemas import Message


class ConversationManager:

    def needs_clarification(self, messages: List[Message]) -> bool:
        """
        Decide whether we have enough information
        to recommend assessments.
        """

        latest_message = messages[-1].content.lower()

        keywords = [
            "java",
            "python",
            "developer",
            "engineer",
            "manager",
            "sales",
            "analyst",
            "leader",
        ]

        return not any(word in latest_message for word in keywords)

    def clarification_question(self) -> str:
        return (
            "Could you tell me which role you're hiring for "
            "and the experience level?"
        )