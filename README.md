# Project B – Automated Content Generation Workflow

## Aim
Develop a web application that creates different types of content from structured user requirements.

## Features
- Blog article, social media post, professional email, essay, and product description.
- Tone, target audience, and length selection.
- Optional additional instructions.
- Generated content preview.
- Download result as a TXT file.
- Demo mode works without an API key; live AI generation is enabled by configuring an OpenAI API key.

## Technology
Python 3.10+, Streamlit, OpenAI Python SDK.

## Run on a laptop

1. Install Python 3.10 or newer.
2. Extract this ZIP and open a terminal in the extracted folder.
3. Create a virtual environment (optional but recommended):
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Optional live AI: copy `.env.example` to `.env` and add your own API key. Never share or commit this file. Without a key, the app runs in demo mode.
6. Start: `streamlit run app.py`
7. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Run on Android
Deploy the project from GitHub using Streamlit Community Cloud, then open its app URL in Chrome. The app is responsive and does not require Python on Android.

## GitHub upload

Create a new GitHub repository named `automated-content-generator`. Upload the contents of this folder (not the ZIP itself), then commit the files.

Alternatively, from a terminal:
```bash
git init
git add .
git commit -m "Add automated content generation project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/automated-content-generator.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your GitHub username.

## Streamlit Community Cloud deployment
1. Sign in at https://share.streamlit.io/ using GitHub.
2. Choose **Create app** and select your repository.
3. Branch: `main`; main file: `app.py`.
4. Deploy. To enable live AI, add `OPENAI_API_KEY = "your-key"` in the app's Secrets settings. Keep the key private.
5. The app runs in demo mode if no key is configured.

## Test cases
1. Select Blog article and enter "Artificial Intelligence in Education".
2. Select Professional tone and College students as the audience.
3. Generate and review the output.
4. Change content type to Social media post and compare the output.
5. Download the TXT file.

## Result
A working content-generation workflow demonstrates how structured prompt templates automate draft creation.
