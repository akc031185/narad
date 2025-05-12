import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from agent_runner import run_all_agents

def main():
    print("🚀 Orchestrator starting...\n")
    run_all_agents()

if __name__ == "__main__":
    main()
