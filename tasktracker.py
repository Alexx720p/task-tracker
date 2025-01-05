import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
   if os.path.exists(TASKS_FILE):
      with open(TASKS_FILE, 'r') as file:
            return json.load(file)
   return []

def save_tasks(tasks):
   with open(TASKS_FILE, 'w') as file:
      json.dump(tasks, file, indent=4)

def add_task(description):
   tasks = load_tasks()
   task_id = len(tasks) + 1
   task = {
      'id': task_id,
      'description': description,
      'status': 'todo',
      'createdAt': datetime.now().isoformat(),
      'updatedAt': datetime.now().isoformat()
   }
   tasks.append(task)
   save_tasks(tasks)
   print(f'Task added successfully (ID: {task_id})')

def list_tasks():
   tasks = load_tasks()
   for task in tasks:
      print(f"{task['id']}: {task['description']} [{task['status']}]")

def update_task(task_id, description):
   tasks = load_tasks()
   for task in tasks:
      if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated successfully')
            return
   print(f'Task {task_id} not found')

def delete_task(task_id):
   tasks = load_tasks()
   tasks = [task for task in tasks if task['id'] != task_id]
   save_tasks(tasks)
   print(f'Task {task_id} deleted successfully')

def mark_task(task_id, status):
   tasks = load_tasks()
   for task in tasks:
      if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}')
            return
   print(f'Task {task_id} not found')

if __name__ == '__main__':
   import sys
   command = sys.argv[1]
   if command == 'add':
      add_task(sys.argv[2])
   elif command == 'list':
      list_tasks()
   elif command == 'update':
      update_task(int(sys.argv[2]), sys.argv[3])
   elif command == 'delete':
      delete_task(int(sys.argv[2]))
   elif command == 'mark':
      mark_task(int(sys.argv[2]), sys.argv[3])
   else:
      print('Unknown command')
