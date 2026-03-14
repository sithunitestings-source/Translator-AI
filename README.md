<img width="1919" height="963" alt="Project Banner" src="https://github.com/user-attachments/assets/410be19c-79c6-448f-ada2-1cdbfcde7456" />

# ADK Translator Agent - Setup & Deployment Guide

An AI-powered translation tool built for the Google Cloud Hackathon, leveraging the speed of **Gemini 1.5 Flash** and the scalability of **Google Cloud Run**.

---

## 📺 Project Demo & Proof of Deployment
Check out the project in action and see the backend configuration:
* **YouTube Demo:** [Watch the Video](https://youtu.be/IaT4qtllLss)
* **Live Service URL:** [Access the App Here](https://adk-translator-agent-640504291333.us-central1.run.app/)

---

## 🛠️ Google Cloud Services Used
- **Gemini 1.5 Flash:** High-speed LLM used for precise, context-aware translations.
- **Cloud Run:** Serverless platform used to host the containerized application.
- **Cloud Build:** Automates the creation of Docker images from source code.
- **Artifact Registry:** Securely stores and manages our container images.

---

## 💻 Local Setup
To run this project locally for testing:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sithunitestings-source/Translator-AI.git](https://github.com/sithunitestings-source/Translator-AI.git)
   cd Translator-AI


2. Install dependencies: ```bash
pip install -r requirements.txt

3.
 ```bash
  python main.py
```

☁️ Deployment Instructions
Follow these steps to deploy the project to your own Google Cloud environment:

1. Initialize Google Cloud Shell
Ensure you are in the project directory and your project ID is set:

```bash
gcloud config set project hackathon-program-adk-bot
```
2. Enable Required APIs
```bash
gcloud services enable run.googleapis.com \
    artifactregistry.googleapis.com \
    cloudbuild.googleapis.com
```
3. Build & Push Image
Use Cloud Build to containerize the app and push it to the registry:

```bash
gcloud builds submit --tag gcr.io/hackathon-program-adk-bot/adk-translator-agent .
```

4. Deploy to Cloud Run
Deploy the image as a public service:
```bash
gcloud run deploy adk-translator-agent \
  --image gcr.io/hackathon-program-adk-bot/adk-translator-agent \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```
  
📂 Project Structure
main.py: Flask backend integrating the Gemini API.

index.html: Clean frontend interface for user interaction.

Dockerfile: Container configuration for Google Cloud deployment.

requirements.txt: Python dependencies (Flask, google-generativeai, etc.).

Developed by Sithuni Nudara for the Google Cloud Hackathon 2026.
