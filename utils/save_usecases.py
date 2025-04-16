import os


def save_to_markdown(company, industry, strategy, usecases):
    os.makedirs("data", exist_ok=True)
    file_path = "data/usecases.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# AI Use Case Report for {company}\n\n")
        f.write(f"**Industry:** {industry}\n\n")
        f.write("## 🧠 Market Research Summary\n")
        f.write(strategy + "\n\n")
        f.write("## 💡 Suggested AI/GenAI Use Cases\n")
        f.write(usecases + "\n")

    return file_path
