# Financial Document Analyzer

A multi-agent financial document analysis system built using **FastAPI, CrewAI, Ollama (LLaMA3), and SQLite**.

This system allows users to upload financial PDF reports and receive structured investment insights using a locally running LLM.

---

## Overview

This project implements an AI-powered financial document analysis backend that:

- Accepts financial PDF uploads
- Extracts text from documents
- Uses CrewAI multi-agent orchestration
- Runs a Local LLM (Ollama LLaMA3)
- Generates structured investment analysis
- Stores results in SQLite database
- Returns JSON API response

The system is fully local and does not require paid API keys.

---

## Tech Stack

- **FastAPI** – REST API framework
- **CrewAI** – Multi-agent orchestration
- **Ollama (LLaMA3)** – Local Large Language Model
- **SQLite** – Persistent database storage
- **pdfplumber** – PDF text extraction
- **LiteLLM** – LLM routing layer

---

## System Architecture

### Flow:

1. User uploads financial PDF via `/analyze`
2. PDF text extracted using `pdfplumber`
3. CrewAI Agent processes document
4. Ollama LLaMA3 generates analysis
5. Result stored in SQLite database
6. JSON response returned to user
