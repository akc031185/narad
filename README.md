#  🧠 Narad: Agentic AI System for Life Automation

Narad is a modular AI system to manage work, learning, fitness, and calendar optimization through intelligent agents.

## 📁 Project Structure

apps/ # Frontend apps (mobile/web)
backend/ # AI agents, APIs, orchestrator
data/ # DB schema, memory stores, logs
infra/ # Docker, K8s, Terraform
tests/ # Unit and integration tests
.github/ # CI/CD workflows


Each agent lives in its own folder, managed by a central orchestrator with optional long-term memory and scheduling.

## 🚀 Setup

To run locally:

```bash
docker-compose up --build

Python 3.11 + FastAPI

Docker & Kubernetes

PostgreSQL & Chroma DB

Terraform for Infra

React Native (mobile), Next.js (web)

