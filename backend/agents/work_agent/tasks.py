def fetch_todo_items():
    # Later: connect to Jira, Trello, Notion, etc.
    return [
        {"title": "Finish backend API", "status": "in progress"},
        {"title": "Prepare DSA problem set", "status": "pending"},
        {"title": "Respond to design team", "status": "pending"}
    ]

def summarize_tasks(tasks):
    return "\n".join([f"- {task['title']} ({task['status']})" for task in tasks])
