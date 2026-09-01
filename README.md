# 🥀 Wingman AI

A modular dating intelligence demo built with Streamlit, FastAPI, local RAG, NLP signal analysis, screenshot OCR and SQLite.

## Run

```powershell
py -3.13 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## API

```powershell
uvicorn api:app --reload
```

Swagger: http://127.0.0.1:8000/docs

## Screenshot OCR

The screenshot feature uses pytesseract. The Tesseract Windows executable must also be installed and available on PATH.

## RAG

knowledge_base.json is the local knowledge base. core/rag.py retrieves relevant entries with TF-IDF + cosine similarity.
