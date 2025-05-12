from .tasks import fetch_todo_items, summarize_tasks
from .planner import generate_daily_plan


def run_work_agent():
    print("👨‍💻 Running Work Agent...")

    todos = fetch_todo_items()
    summary = summarize_tasks(todos)

    plan = generate_daily_plan(summary)

    print("📋 Today's Plan:")
    print(plan)

if __name__ == "__main__":
    run_work_agent()