import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class UseCaseAgent:
    def __init__(self, company_name, industry, strategy_summary):
        self.company_name = company_name
        self.industry = industry
        self.strategy_summary = strategy_summary
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def run(self):
        prompt = f"""
        Based on the following company strategy and industry:
        Company: {self.company_name}
        Industry: {self.industry}
        Strategy Summary: {self.strategy_summary}

        🔍 Generate 5-6 relevant AI/ML/GenAI use cases this company could benefit from.
        🎯 Focus on improving operations, customer experience, automation, or analytics.
        Include short descriptions for each use case.
        """
        response = self.model.generate_content(prompt)
        return response.text


if __name__ == "__main__":
    dummy_strategy = "Nike focuses on personalized retail experience, supply chain optimization, and direct-to-consumer sales."
    agent = UseCaseAgent(company_name="Nike", industry="Retail", strategy_summary=dummy_strategy)
    print(agent.run())
