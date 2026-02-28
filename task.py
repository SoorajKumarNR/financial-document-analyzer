# task.py

from crewai import Task
from agents import financial_analyst

analysis_task = Task(
    description=(
        "You are given this financial document text:\n\n"
        "{document_text}\n\n"
        "User Query:\n"
        "{query}\n\n"
        "Based strictly on the above text, provide a structured analysis including:\n"
        "1. Revenue trends\n"
        "2. Net income summary\n"
        "3. Cash flow insights\n"
        "4. Key risks\n"
        "5. Investment outlook\n\n"
        "Do not invent information not present in the document."
    ),
    expected_output=(
        "Structured analysis based solely on provided document text."
    ),
    agent=financial_analyst,
    async_execution=False
)