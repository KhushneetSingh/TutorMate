# DEV OPS GUIDE (PRIVATE)

This file is a **personal development & operations guide**.
It explains how to start, stop, restart, and test the project
using **Docker (Redis)** and **local Python execution**.

This file is NOT meant to be published.

---

## CORE PRINCIPLE

- Redis = STATEFUL (runs in Docker)
- Agents = STATELESS (run locally during dev)
- Docker is infrastructure, not logic

---

## 1. FIRST-TIME SETUP

### 1.1 Create `.env`
```env
GOOGLE_API_KEY=your_api_key_here
REDIS_URL=redis://localhost:6379/0
```

Never commit `.env`.

---

## 2. START REDIS (DOCKER)

Redis should run continuously during development.

**Start Redis container:**
```bash
docker run -d --name tutormate-redis -p 6379:6379 redis
```

**Verify:**
```bash
docker ps
```

Expected: `tutormate-redis` is running.

---

## 3. CHECK .env in CLI 
```bash
export $(cat .env | xargs)
```

```bash
echo $GOOGLE_API_KEY
echo $REDIS_URL
```

Expected:
```
sju7yd83hjbd83hdb8dh3dhw
redis://localhost:6379/0
```

---

## 4. RUN AGENT SYSTEM (LOCAL)

Agents are run locally for debugging clarity.
```bash
export PYTHONPATH = .
```
```bash
python run_planner.py
```

**What this does:**
- Initializes agent(s)
- Connects to Redis memory
- Reads/writes persistent state

---

## 5. NORMAL DEV WORKFLOW

**Daily workflow:**

1. Start Redis (once)
2. Run agent
3. Stop agent
4. Modify logic
5. Run agent again

Redis stays running the entire time.

---

## 6. STOP / RESTART RULES

**Stop agent:**
```bash
Ctrl + C
```

**Stop Redis (keep data):**
```bash
docker stop tutormate-redis
```

**Restart Redis (data persists):**
```bash
docker start tutormate-redis
```

---

## 7. RESET MEMORY (DEVELOPMENT ONLY)

⚠️ This deletes all agent memory.
```bash
docker stop tutormate-redis
docker rm tutormate-redis
```

**Start fresh:**
```bash
docker run -d --name tutormate-redis -p 6379:6379 redis
```

**Use this to test:**
- first-time users
- cold starts
- memory initialization

---

## 8. TESTING SCENARIOS

### 8.1 Cold Start Test
- Redis restarted
- Agent run once
- Expect: fresh memory

### 8.2 Warm Start Test
- Redis running
- Agent run multiple times
- Expect: memory reuse, no duplication

### 8.3 Crash Recovery
- Kill agent mid-run
- Restart agent
- Expect: system resumes safely

---

## 9. DOCKER USAGE POLICY

| Component | Docker? |
|-----------|---------|
| Redis | ✅ Always |
| Agents (dev) | ❌ |
| Agents (integration) | ✅ |
| Final demo | ✅ |

---

## 10. WHEN TO CONTAINERIZE AGENTS

Only after:
- Memory behavior is correct
- Agent lifecycle is stable
- Failure modes are understood

---

## REMINDER

If something behaves oddly:
- Inspect Redis
- Do NOT add features
- Fix lifecycle first