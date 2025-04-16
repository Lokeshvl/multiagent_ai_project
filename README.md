# 🧠 AI/GenAI Use Case Generation System – Multi-Agent Architecture

## 📌 Objective

This project implements a multi-agent system that performs:
- Industry research
- Strategic insight extraction
- Use case generation
- Dataset mapping

All tailored for a given company/industry using Generative AI (Gemini Pro).

---

## 🏗️ System Architecture

**Flow of agents:**

1. User inputs company and industry.
2. **Research Agent** identifies the company’s strategic focus.
3. **Use Case Agent** suggests GenAI/ML use cases.
4. **Resource Agent** finds dataset resources from Kaggle, HuggingFace, GitHub.
5. Results are saved in a markdown file.

### 📌 Architecture Diagram

![image](https://github.com/user-attachments/assets/b5485b6b-e01c-4f3a-b49d-51cd4d2ff58f)

---

## 🧠 Agents & Responsibilities

### 🔍 Research Agent
- Uses Gemini API to understand market trends, strategic goals, and industry focus.

### 💡 Use Case Agent
- Based on research, it generates company-relevant AI/ML use cases.
- Focus: customer experience, operational efficiency, automation, etc.

### 🔗 Resource Agent
- Suggests dataset links or search queries for each use case.
- Uses Google search with Kaggle, HuggingFace, and GitHub constraints.

---

## 💼 Sample Input

- **Company**: Nike  
- **Industry**: Retail

---

## 💡 Sample Use Cases Generated

1. **AI Inventory Forecasting**  
   Automate and optimize stock prediction using time-series ML models.

2. **Virtual Fashion Assistant (GenAI)**  
   Suggest fashion items using conversational AI trained on product catalogs.

3. **Customer Support Chatbot**  
   NLP model trained on historical chat logs for 24/7 customer service.

4. **GenAI for Product Descriptions**  
   Automate product listing creation using LLMs.

5. **AI-powered Visual Search**  
   Upload image → get similar Nike products using computer vision.

---

## 🔗 Dataset Resources

Example searches:
- [Search Kaggle for Inventory Forecasting](https://www.google.com/search?q=inventory+forecasting+dataset+site:kaggle.com)
- [Search HuggingFace for Chatbot Datasets](https://www.google.com/search?q=chatbot+dataset+site:huggingface.co)
- [Search GitHub for Visual Search Models](https://www.google.com/search?q=visual+search+AI+site:github.com)

---

## ✅ Deliverables

| Component           | Status  |
|--------------------|---------|
| Multi-Agent Logic  | ✅ Done |
| Markdown Output    | ✅ Done |
| Architecture Flow  | ✅ Done |
| Gemini Integration | ✅ Done |
| Dataset Suggestions| ✅ Done |
| UI (Streamlit App) | ✅ Done |
| Report             | ✅ Done |

---

## 🔮 Future Work

- Add real-time search scraping APIs (Tavily, Serper)
- Connect to live Kaggle API for auto-retrieval
- Export to PDF or Notion
- Integrate with RAG pipelines (LangChain or LlamaIndex)

---

## 📚 References

- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [Kaggle Datasets](https://kaggle.com)
- [DeepLearning.ai – Multi-Agent Systems](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- [McKinsey Report: AI in Retail](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/ai-in-retail)

