# Study Buddy Agent (study-buddy-agent)

## What is it?
Study Buddy is an AI-powered study assistant that converts PDFs/images into concise study notes, generates personalized study plans, tutors via Q/A, and tracks your learning progress.

## Features (MVP)
- OCR extraction (PDF/image)
- Notes generation
- Study plan generator
- Q/A tutor with context
- Progress tracking

## Tech stack
- Frontend: Next.js + Tailwind
- Backend: FastAPI (Python)
- Worker: Celery + Redis
- DB: PostgreSQL
- OCR: Tesseract / Google Vision
- LLM: OpenAI API

## Quickstart
1. `git clone https://github.com/<you>/study-buddy-agent.git`
2. Backend: `cd backend && pip install -r requirements.txt`
3. Start services: Redis, Postgres
4. `uvicorn app.main:app --reload`
5. Frontend: `cd frontend && npm install && npm run dev`

## Demo
See `notebooks/demo.ipynb` with sample inputs & outputs.

## Contributing
PRs welcome. Use `dev` branch for feature work.

## License
MIT