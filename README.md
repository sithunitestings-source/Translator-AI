<img width="1919" height="963" alt="image" src="https://github.com/user-attachments/assets/410be19c-79c6-448f-ada2-1cdbfcde7456" />
# ADK Translator Agent - Setup & Deployment Guide

This project is an AI-powered translator built using Google Gemini and deployed on Google Cloud Run.

## Local Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python main.py`

## Google Cloud Deployment (Cloud Run)
To deploy this project to Google Cloud, follow these steps in your Cloud Shell:

1. **Enable APIs:**
   `gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com`

2. **Build the Image:**
   `gcloud builds submit --tag gcr.io/[PROJECT_ID]/adk-translator-agent .`

3. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy adk-translator-agent \
     --image gcr.io/[PROJECT_ID]/adk-translator-agent \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
https://adk-translator-agent-640504291333.us-central1.run.app/
