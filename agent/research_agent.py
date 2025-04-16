import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

class ResearchAgent:
    def __init__(self, company_name, industry=None):
        self.company_name = company_name
        self.industry = industry
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def run(self):
        query = f"""
        Conduct market research on {self.company_name} in the {self.industry or "relevant"} industry. Identify their 
        AI strategy, focus areas (e.g., operations, supply chain), and potential opportunities for GenAI integration."""
        response = self.model.generate_content(query)
        return response.text



if __name__ == "__main__":
    agent = ResearchAgent(company_name="Nike", industry="Retail")
    summary = agent.run()
    print(summary)
