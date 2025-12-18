# Study Buddy Agent 🤖📚

An **agent-based AI study companion** designed to help learners plan,
study, revise, and track academic progress using **persistent memory**
and **coordinated AI agents**.

This project explores how **multi-agent systems** can be applied responsibly
to education.

---

## 🌍 Project Overview

Study Buddy Agent is built around the idea that learning support should be:

- **Personalized** (adapts to the learner)
- **Persistent** (remembers context & progress)
- **Modular** (multiple specialized agents)
- **Explainable** (clear system boundaries)

The system uses **Redis-backed memory**, **LLMs**, and an
**agent-to-agent (A2A) architecture** to coordinate learning tasks.

---

## 🧠 Core Capabilities (Planned)

- Study plan generation & adaptation
- Question–answer tutoring (RAG-based)
- Content ingestion (PDFs, notes, images)
- Progress tracking & reminders
- Multi-agent coordination
- Observability & telemetry

---

## 🏗️ High-Level Architecture

- **Stateless agents** handle reasoning and actions
- **Stateful memory** is stored externally (Redis, Vector DB)
- **Coordinator agent** routes tasks between agents
- **Infrastructure** is containerized using Docker

## 🗂️ Project Structure (Planned)
```
study-buddy-agent/
├── infra/
│   └── docker-compose.yml          # Redis, vector DB, infra services
├── app/
│   ├── agents/
│   │   ├── planner_agent.py        # creates & adapts study plans
│   │   ├── tutor_agent.py          # Q&A tutor (RAG-based)
│   │   ├── content_agent.py        # OCR, PDF parsing, chunking
│   │   ├── progress_agent.py       # tracks progress & triggers updates
│   │   ├── coordinator.py          # agent-to-agent router (A2A brain)
│   │   └── base_agent.py           # shared agent interface
│   ├── tools/
│   │   ├── registry.py             # tool discovery & routing
│   │   ├── ocr_tool.py
│   │   ├── pdf_tool.py
│   │   ├── embedding_tool.py       # embeddings for retrieval
│   │   └── schedule_tool.py
│   ├── memory/
│   │   ├── redis_memory.py         # short-term & session memory
│   │   └── vector_store.py         # FAISS / Chroma (long-term memory)
│   ├── observability/
│   │   └── telemetry.py            # logging, tracing, metrics
│   ├── a2a/
│   │   └── mqtt_a2a.py             # agent-to-agent messaging
│   ├── api/
│   │   ├── study.py                # study endpoints
│   │   ├── upload.py               # content ingestion
│   │   └── chat.py                 # conversational interface
│   └── main.py                     # application entry point
├── README.md
```

## 🔧 Tech Stack

- Python
- Redis
- Docker & Docker Compose
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Agent-based architecture

---

## 🚦 Project Status

🟡 **Active Development (Architecture Phase)**

- Core agent abstractions defined
- Redis-backed memory integrated
- Agent lifecycle & recovery testing in progress
- Infrastructure-first approach

---

## 🔐 Security & Configuration

- Secrets managed via `.env`
- No credentials committed
- Redis used locally during development

---

## 🎯 Goals

- Demonstrate real-world agent orchestration
- Build reliable, restart-safe AI systems
- Explore AI agents for education (Agents for Good)

---

## 👤 Author

**Khushneet Singh**  
AI Agents Capstone Project

---

## 📌 Note

This repository is under active development.
Interfaces, agents, and infrastructure may evolve.