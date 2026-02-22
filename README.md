\# 🚦 Teknocity MVP



AI-powered Urban Traffic Optimization System

Hackathon Project – 20 Days



---



\## 📌 Project Overview



Teknocity is an intelligent traffic optimization system designed to:



\- Simulate urban traffic scenarios

\- Compare fixed traffic light control vs RL-based control

\- Store reproducible experiment results

\- Provide real-time comparison metrics

\- Serve a dashboard for visualization



This project follows a modular architecture.



---



\## 🏗 Repository Structure

teknocity-mvp/

│

├── backend/ # FastAPI + PostgreSQL (Orchestrator)

├── ai/ # Reinforcement Learning model

├── simulation/ # SUMO configuration

├── frontend/ # React dashboard

└── docs/ # Documentation



---



\## 🧠 Backend Responsibilities



The backend is the central orchestrator.



It will:



\- Execute simulations (baseline + RL)

\- Load trained models (.pth)

\- Calculate official metrics

\- Store experiments in PostgreSQL

\- Provide comparison endpoints



---



\## 🔀 Git Workflow



Main branch is protected.



Workflow:



feature/\* → dev → main



Rules:



\- No direct push to main

\- Pull Request required for merging

\- All work must be done in feature branches



---



\## 🛠 Local Development



\### Backend

cd backend

python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt





---



\## 📅 Development Phases



\### Phase 1 – MVP (Mandatory)

\- PostgreSQL (Docker)

\- Experiment model

\- /simulate endpoint

\- /compare endpoint

\- Database storage



\### Phase 2 – SUMO + RL Integration

\- Execute SUMO from backend

\- Load RL model

\- Extract metrics from tripinfo.xml



\### Phase 3 – Hardening

\- Logging

\- Error handling

\- Dockerization

\- Deployment preparation



---



\## 🎯 Goal



Even if full integration is not completed,

Phase 1 must result in a reproducible and presentable MVP.

