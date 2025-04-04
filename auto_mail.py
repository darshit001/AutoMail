import requests
from datetime import datetime
import urllib.parse

WEBHOOK_URL = "https://avdfasdfsdffdaas.app.n8n.cloud/webhook/daily-task-report"  # Use the production URL

TASKS_FILE = "daily_tasks.txt"

def read_tasks_from_file():
    with open(TASKS_FILE, 'r') as f:
        tasks = f.read().strip()
    return tasks

def send_webhook_request(tasks):
    """Send the tasks to the n8n Webhook URL using a GET request."""
    encoded_tasks = urllib.parse.quote(tasks)
    url = f"{WEBHOOK_URL}?raw_tasks={encoded_tasks}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[{datetime.now()}] Webhook request sent successfully! Workflow is running...")
        else:
            print(f"[{datetime.now()}] Failed to send Webhook request. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"[{datetime.now()}] Error sending Webhook request: {e}")

def main():
    tasks = read_tasks_from_file()
    
    if tasks:
        print(f"[{datetime.now()}] Triggering workflow with tasks: {tasks}")
        send_webhook_request(tasks)
    else:
        print(f"[{datetime.now()}] No tasks to process.")

if __name__ == "__main__":
    main()
