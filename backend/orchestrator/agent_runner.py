import importlib

AGENTS = [
    "backend.agents.work_agent.agent"
    # Add more agents here later
]

def run_all_agents():
    for agent_path in AGENTS:
        print(f"⚙️ Launching {agent_path}...")
        try:
            agent_module = importlib.import_module(agent_path)
            if hasattr(agent_module, "run_work_agent"):
                agent_module.run_work_agent()
            else:
                print(f"❌ {agent_path} has no run_work_agent()")
        except Exception as e:
            print(f"🔥 Failed to run {agent_path}: {e}")
