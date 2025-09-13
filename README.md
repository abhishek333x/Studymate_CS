# StudyMate Hub

A full-stack AI-powered student assistant with PDF Q&A, OCR, flashcards, quizzes, podcast mode, and more.

## Folder Structure

- `backend/` — FastAPI backend
- `frontend/` — Streamlit frontend
- `data/` — SQLite DB (auto-created)
- `requirements.txt` — All dependencies

## Setup & Run

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Keys**  
   - Copy `.env.example` to `.env` and fill in your real API keys:
     ```
     cp .env.example .env
     ```
   - Edit `.env` and add your keys for IBM, OpenAI, HuggingFace, ElevenLabs, etc.

3. **Start backend**  
   ```bash
   uvicorn backend.main:app --reload
   ```
   (The backend will automatically load environment variables using `python-dotenv`.)

4. **Start frontend**  
   ```bash
   streamlit run frontend/streamlit_app.py
   ```
   # (If your frontend file is named differently, adjust the filename accordingly.)

5. **Open**  
   - Backend: http://127.0.0.1:8000/docs  
   - Frontend: http://localhost:8501

## How to View the User Interface

1. Start your backend:
   ```bash
   uvicorn backend.main:app --reload
   ```

2. Start your frontend:
   ```bash
   streamlit run frontend/streamlit_app.py
   ```

3. Open your web browser and go to:
   ```
   http://localhost:8501
   ```
   (Or use the network address shown in your terminal if running on a remote server.)

## How to Test StudyMate Hub

1. **Start the backend:**
   ```bash
   uvicorn backend.main:app --reload
   ```

2. **Start the frontend:**
   ```bash
   streamlit run frontend/streamlit_app.py
   ```

3. **Open your browser:**
   - Go to [http://localhost:8501](http://localhost:8501) for the StudyMate Hub UI.
   - Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for backend API docs.

4. **Test features:**
   - Use the UI to upload PDFs, images, text, or Word files.
   - Ask questions in the PDF Q&A tab to test Hugging Face model integration.
   - Try other tabs (OCR, Flashcards, Quizzes, Podcast, etc.).

5. **Check for errors:**
   - If any errors occur, check your terminal for backend/Streamlit logs.
   - Ensure your `.env` file contains valid API keys/tokens.

## Important Notes

- Some advanced features (Podcast, Mentor, Mind-map, etc.) are currently stubs or placeholders.
- These will only work after integrating with real AI APIs or services.
- For demo, use core features like PDF Q&A, OCR, Flashcards, and Quizzes.

## Features

- Multi-input Q&A (PDF, image, text, Word)
- Camera OCR
- Flashcards & quizzes
- Podcast story mode (TTS)
- Summaries, notes, references
- AI mentor personas

## What are `.env` and `.env.example`?

- **.env.example**  
  This is a template file listing all the environment variables your project needs (like API keys).  
  It does not contain real secrets—just empty values or placeholders.

- **.env**  
  This file contains your actual secret keys and configuration values.  
  You copy `.env.example` to `.env` and fill in your real API keys.

**Example:**

.env.example
```
IBM_API_KEY=
OPENAI_API_KEY=
HUGGINGFACE_API_KEY=
ELEVENLABS_API_KEY=
```

.env (do not share this file)
```
IBM_API_KEY=your_real_ibm_key
OPENAI_API_KEY=your_real_openai_key
HUGGINGFACE_API_KEY=your_real_hf_key
ELEVENLABS_API_KEY=your_real_elevenlabs_key
```

**Never commit your `.env` file to version control. Only commit `.env.example`.**

---

**For hackathon demo:**  
- Use the sidebar to explore all features.

---
