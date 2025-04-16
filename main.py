from agent.research_agent import ResearchAgent
from agent.usecase_agent import UseCaseAgent
from agent.resource_agent import ResourceAgent


def main():
    company_name = "Nike"
    industry = "Retail"


    print("🔍 Running Research Agent...")
    research_agent = ResearchAgent(company_name, industry)
    strategy = research_agent.run()
    print(strategy)


    print("\n📊 Running Use Case Agent...")
    usecase_agent = UseCaseAgent(company_name, industry, strategy)
    usecases_text = usecase_agent.run()
    print(usecases_text)


    print("\n📦 Running Resource Agent...")
    sample_usecases = [
        "AI-powered inventory forecasting",
        "GenAI fashion assistant",
        "Customer support chatbot"
    ]
    resource_agent = ResourceAgent(sample_usecases)
    resource_agent.search_datasets()

if __name__ == "__main__":
    main()
