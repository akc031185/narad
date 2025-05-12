from fastapi import FastAPI
from agent_runner import run_all_agents

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Narad Orchestrator is running."}

@app.post("/run-all")
def run_all():
    run_all_agents()
    return {"status": "All agents executed."}

@app.get("/health")
def health():
    return {"status": "ok"}
