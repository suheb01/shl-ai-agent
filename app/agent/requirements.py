from typing import List, Optional

from pydantic import BaseModel


class HiringRequirements(BaseModel):
    """
    Stores all information extracted
    from the user's conversation.
    """

    role: Optional[str] = None

    seniority: Optional[str] = None

    experience: Optional[str] = None

    skills: List[str] = []

    personality_required: bool = False

    cognitive_required: bool = False

import re

from app.models.schemas import Message


class RequirementExtractor:
    """
    Extract hiring requirements from the conversation.
    """

    def extract(self, messages: list[Message]) -> HiringRequirements:

        requirements = HiringRequirements()

        conversation = " ".join(
            message.content.lower()
            for message in messages
            if message.role == "user"
        )

        # -------- Role Detection --------
        if "java" in conversation:
            requirements.role = "Java Developer"
            requirements.skills.append("Java")

        elif "python" in conversation:
            requirements.role = "Python Developer"
            requirements.skills.append("Python")

        elif "data analyst" in conversation:
            requirements.role = "Data Analyst"

        elif "sales" in conversation:
            requirements.role = "Sales"

        # -------- Seniority --------
        if "senior" in conversation:
            requirements.seniority = "Senior"

        elif "junior" in conversation:
            requirements.seniority = "Junior"

        elif "lead" in conversation:
            requirements.seniority = "Lead"

        # -------- Experience --------
        match = re.search(r"(\d+)\s*(year|years)", conversation)

        if match:
            requirements.experience = f"{match.group(1)} years"

        # -------- Assessment Preferences --------
        if "personality" in conversation:
            requirements.personality_required = True

        if "cognitive" in conversation:
            requirements.cognitive_required = True

        return requirements