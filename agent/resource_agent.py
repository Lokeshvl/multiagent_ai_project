import webbrowser

class ResourceAgent:
    def __init__(self, usecases: list):
        self.usecases = usecases

    def search_datasets(self):
        for usecase in self.usecases:
            query = usecase + " dataset site:kaggle.com OR site:huggingface.co OR site:github.com"
            print(f"🔍 Searching datasets for: {usecase}")
            webbrowser.open(f"https://www.google.com/search?q={query}")


if __name__ == "__main__":
    sample_usecases = [
        "AI-powered inventory forecasting",
        "GenAI virtual fashion assistant",
        "Customer support chatbot for retail"
    ]
    agent = ResourceAgent(sample_usecases)
    agent.search_datasets()
