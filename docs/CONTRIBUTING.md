# Contribution Guidelines – Teknocity MVP

## 🔀 Branching Strategy

- main → Stable
- dev → Integration
- feature/* → Individual work

Example:

feature/backend-simulation
feature/frontend-dashboard
feature/rl-agent
feature/sumo-config

---

## 🧠 Module Ownership

Each team member must work only inside their module:

- backend/ → Backend Lead
- ai/ → AI Team
- simulation/ → Simulation Team
- frontend/ → Frontend Team

No cross-module modifications without coordination.

---

## 🛠 Environment Rules

Each module must have its own virtual environment.

Never commit:

- venv/
- node_modules/
- large model files
- datasets

---

## 📌 Commit Rules

Commits must be clear and in English.

Good example:

Add initial experiment model
Implement simulation runner
Configure PostgreSQL connection

Bad example:

update
changes
fix