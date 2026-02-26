import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import vertexai
from vertexai.generative_models import GenerativeModel
import sqlalchemy

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CONFIGURATION ---
PROJECT_ID = "hackathon-program-adk-bot"
REGION = "us-central1"
DB_PASS = os.getenv("DB_PASS", "default_password_if_missing")
DB_HOST = "10.209.0.3"

vertexai.init(project="hackathon-program-adk-bot", location="us-central1")
model = GenerativeModel("gemini-2.5-flash")


engine = sqlalchemy.create_engine(
    f"postgresql+pg8000://postgres:{DB_PASS}@{DB_HOST}/postgres",
    connect_args={"login_timeout": 2}
)

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("index.html", "r") as f:
        return f.read()

@app.post("/translate")
async def translate_text(request: Request):
    try:
        data = await request.json()
        text = data.get("text")
        target_lang = data.get("target", "Sinhala")

        # 1. Generate Translation
        prompt = f"Translate the following text to {target_lang}. Only return the translation: {text}"
        response = model.generate_content(prompt)
        translated_text = response.text

        # 2. Attempt Database Log 
        try:
            with engine.connect() as conn:
                # Create table if it's missing
                conn.execute(sqlalchemy.text("CREATE TABLE IF NOT EXISTS translation_logs (id SERIAL PRIMARY KEY, original TEXT, translated TEXT)"))
                conn.execute(
                    sqlalchemy.text("INSERT INTO translation_logs (original, translated) VALUES (:o, :t)"),
                    {"o": text, "t": translated_text}
                )
                conn.commit()
        except Exception as db_err:
            print(f"Database error (skipped): {db_err}")

        return {"translated_text": translated_text}

    except Exception as e:
        
        return {"translated_text": f"Error: {str(e)}"}