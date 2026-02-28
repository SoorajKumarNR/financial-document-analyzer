# main.py

from fastapi import FastAPI, File, UploadFile, Form, HTTPException, BackgroundTasks
import os
import uuid
import pdfplumber

from crewai import Crew, Process
from agents import financial_analyst
from task import analysis_task
from database import SessionLocal
from models import AnalysisResult

app = FastAPI(title="Financial Document Analyzer")

# -----------------------
# PDF Text Extraction
# -----------------------
def extract_pdf_text(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text


# -----------------------
# Save Analysis Results
# -----------------------
def save_result_to_db(filename: str, query: str, analysis: str):
    db = SessionLocal()
    record = AnalysisResult(
        filename=filename,
        query=query,
        result=analysis
    )
    db.add(record)
    db.commit()
    db.close()


# -----------------------
# Run Crew
# -----------------------
def run_crew(query: str, document_text: str):
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analysis_task],
        process=Process.sequential,
        verbose=True
    )

    result = financial_crew.kickoff(
        inputs={
            "query": query,
            "document_text": document_text
        }
    )
    return result


# -----------------------
# Health Check
# -----------------------
@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer is running."}


# -----------------------
# Analyze Endpoint
# -----------------------
@app.post("/analyze")
async def analyze_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):

    file_id = str(uuid.uuid4())
    file_path = f"data/{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        document_text = extract_pdf_text(file_path)

        response = run_crew(query=query, document_text=document_text)

        # store in background
        background_tasks.add_task(
            save_result_to_db,
            file.filename,
            query,
            str(response)
        )

        return {
            "status": "success",
            "analysis": str(response)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass