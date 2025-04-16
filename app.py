import streamlit as st
from agent.research_agent import ResearchAgent
from agent.usecase_agent import UseCaseAgent
from agent.resource_agent import ResourceAgent
from utils.save_usecases import save_to_markdown

st.set_page_config(page_title="AI/GenAI Use Case Generator", layout="wide")
st.title("🤖 AI Use Case Generator for Companies")
st.write("Generate tailored AI/GenAI use cases using multi-agents and Gemini.")


company = st.text_input("🏢 Enter Company Name", value="Nike")
industry = st.text_input("🏭 Enter Industry", value="Retail")


if st.button("🚀 Run Multi-Agent System"):
    with st.spinner("Running Research Agent..."):
        research_agent = ResearchAgent(company_name=company, industry=industry)
        strategy = research_agent.run()
        st.subheader("📊 Market Research Summary")
        st.markdown(strategy)

    with st.spinner("Running Use Case Generator..."):
        usecase_agent = UseCaseAgent(company_name=company, industry=industry, strategy_summary=strategy)
        usecases = usecase_agent.run()
        st.subheader("💡 Suggested AI/GenAI Use Cases")
        st.markdown(usecases)

    with st.spinner("Generating Dataset Search Links..."):
        st.subheader("🔗 Suggested Dataset Resources")
        basic_usecases = [
            "AI-powered inventory forecasting",
            "GenAI virtual shopping assistant",
            "Personalized recommendation system",
            "Customer support chatbot",
            "AI-driven product design analysis"
        ]
        for usecase in basic_usecases:
            query = f"{usecase} dataset site:kaggle.com OR site:huggingface.co OR site:github.com"
            st.markdown(f"[🔍 Search Datasets for '{usecase}'](https://www.google.com/search?q={query})")

    # Save to Markdown
    file_path = save_to_markdown(company, industry, strategy, usecases)
    st.success(f"✅ Use case report saved to: `{file_path}`")
