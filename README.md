# Fraud Detector AI Agent  

A project for analyzing **investment offers** and detecting potential **fraud or scam risks**.  
Built with **Python 3.12** and **FastAPI**, structured for clarity, maintainability, evaluation, and fully Dockerized.  

Leverages **LangChain + LLMs** for structured reasoning about risk signals, regulators, and scam indicators.  
Provides both **risk ratings** and **evidence-backed justifications** for transparency.  

---

## Project Structure  

src/              → Core logic (fraud AI agent, schemas, app)  
tests/            → Unit tests for analysis & outputs  
.gitignore        → Ignore artifacts & secrets  
.python-version   → Python 3.12  
pyproject.toml    → Metadata & dependencies  
uv.lock           → Locked deps for reproducibility  
src/Dockerfile    → Containerized API runtime  
README.md         → You’re here  

---

## Overview  

This project helps analyze investment offers by:  

- Detecting **red-flag phrases** and **scam signals**  
- Assigning a **risk rating** (`RED`, `AMBER`, `GREEN`)  
- Returning a **numeric risk score**  
- Providing **human-readable reasons** for the score  
- Linking to **credible evidence sources** when available  
- Exposing a **FastAPI service** for easy integration  

---
## Tools Used

This AI agent combines **rule-based detection** with **AI + web search** to analyze investment offers.

---

### 1. Regex-based Scam Pattern Checker (`pattern_check`)

- Scans the offer text using **regular expressions**.  
- Looks for risky phrases (from `conf.PATTERNS`), like:  
  - "guaranteed returns"  
  - "risk-free investment"  
  - "act now"  
- Each match adds to a **risk score** and a **reason** is logged.  
- Based on thresholds in `conf.THRESHOLDS`:  
  - **RED** → high risk  
  - **AMBER** → medium risk  
  - **GREEN** → low risk  

Provides a fast, rule-based **first layer of fraud detection**.

---

### 2. Tavily Search Tool (`TavilySearchResults`)

- Uses the **Tavily API** to fetch up to **3 credible web results**.  
- Helps verify if a company, investment scheme, or claim has been flagged online.  
- Useful for finding **warnings from regulators, watchdogs, or news sources**.  
- Requires an API key (`TAVILY_API_KEY`) stored in `.env`.

## Getting Started  

### Clone the repository  

```bash
git clone https://github.com/MahsaSin/fraud-detector-AI-agent.git
cd fraud-detector-AI-agent
```
### Running with Docker

The project includes a Dockerfile based on Python 3.12 slim, pre-configured with dependencies like ffmpeg and uv.

**Build the Docker image:**
```bash
cd ..
docker build -t my-fraud-agent-app . -f ./src/Dockerfile
```

**Run the Docker image:**
```bash
docker run -p 8001:8001 --env-file .env my-fraud-agent-app
```

**Once running, the API will be accessible at:**
```bash
http://localhost:8001
```

### Running the app

**Run the app with fastAPI:**
```bash
cd src 
set PYTHONPATH=.
uv run uvicorn app:app --host 0.0.0.0 --port 8001
```

**Run Tests**
```bash
uv run pytest -q
```
