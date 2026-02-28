# agents.py

from crewai import Agent, LLM

# -----------------------------
# Local LLM (Ollama)
# -----------------------------
llm = LLM(
    model="ollama/llama3",
    base_url="http://localhost:11434",
    temperature=0.2
)

# -----------------------------
# Financial Analyst Agent
# -----------------------------
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze the financial document text and provide detailed investment insights.",
    backstory=(
        "You are a Chartered Financial Analyst with expertise in financial statements, "
        "valuation, profitability, risk assessment, and investor communication."
    ),
    verbose=True,
    memory=False,
    allow_delegation=False,
    llm=llm
)