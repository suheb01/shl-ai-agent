import os

import google.generativeai as genai
from dotenv import load_dotenv

from app.agent.prompt_builder import PromptBuilder

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class LLMService:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_recommendation(
        self,
        requirements: dict,
        recommendations: list,
    ) -> str:

        prompt = PromptBuilder.build_recommendation_prompt(
            requirements=requirements,
            recommendations=recommendations,
        )

        try:
            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            print("\n========== Gemini Error ==========")
            print(e)
            return None