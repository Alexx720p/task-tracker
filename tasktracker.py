import json
import os
from datetime import datetime


TASKS_FILE = 'data.json'

def load_tasks():
   '''Load tasks from a file'''
   if os.stat('data.json').st_size == 0:
      return []
   with open('data.json', 'r', encoding='utf-8') as file:
      return json.load(file)

def save_tasks(tasks):
   '''Save tasks to a file'''
   with open(TASKS_FILE, 'w', encoding='utf-8') as file:
      json.dump(tasks, file, indent=4)

def add_task(description):
   '''Add a new task'''
   tasks = load_tasks()
   task_id = len(tasks) + 1
   task = {
      'id': task_id,
      'description': description,
      'status': 'not done',
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

def list_tasks_done():
   tasks = load_tasks()
   for task in tasks:
      if task['status'] == 'done':
            print(f"{task['id']}: {task['description']} [{task['status']}]")
            
def list_tasks_not_done():
   tasks = load_tasks()
   for task in tasks:
      if task['status'] == 'not done':
            print(f"{task['id']}: {task['description']} [{task['status']}]")

def list_tasks_in_progress():
   tasks = load_tasks()
   for task in tasks:
      if task['status'] == 'in progress':
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

def mark_task_as_done(task_id, status):
   tasks = load_tasks()
   for task in tasks:
      if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}')
            return
   print(f'Task {task_id} not found')

def mark_task_as_in_progress(task_id, status):
   tasks = load_tasks()
   for task in tasks:
      if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}')
            return
   print(f'Task {task_id} not found')


menu_options = ('1. Add task',
               '2. List task',
               '3. Update task',
               '4. Delete task',
               '5. Mark task as completed',
               '6. Mark task as in progress',
               '7. Exit')
print(menu_options)

number = input('Enter the number of the task you want to perform: ')

while number != '7':
   print(menu_options)
   number = input('Enter the number of the task you want to perform: ')

   if number == '1':
      add_task(input('Enter the task you want to add: '))

   elif number == '2':
      print('1. List all tasks',
            '2. List tasks done',
            '3. List tasks in progress',
            '4. List tasks not done',
            '5. Exit')
      task_list_number = input('Enter the number of the list you want to perform: ')
      while task_list_number != '5':
         if task_list_number == '1':
            list_tasks()
         elif task_list_number == '2':
            list_tasks_done()
         elif task_list_number == '3':
            list_tasks_in_progress()
         elif task_list_number == '4':
            list_tasks_not_done()
         else:
            print('Invalid input. Please try again.')
         task_list_number = input('Enter the number of the list you want to perform: ')
      print('Back to main menu')

   elif number == '3':
      update_task(int(
                     input('Enter the task id you want to update: ')), 
                     input('Enter the new task: '))
   elif number == '4':
      delete_task(int(input('Enter the task id you want to delete: ')))
   elif number == '5':
      mark_task_as_done(int(input('Enter the task id you want to mark as completed: ')), 'done')
   elif number == '6':
      mark_task_as_in_progress(int(input('Enter the task id you want to mark as in progress: ')), 'in progress')
   else:
      print('Invalid input. Please try again.')

   number = input('Enter the number of the task you want to perform: ')

print('Goodbye!')

# if __name__ == '__main__':
#    import sys
#    command = sys.argv[1]
#    if command == 'add':
#       add_task(sys.argv[2])
#    elif command == 'list':
#       list_tasks()
#    elif command == 'update':
#       update_task(int(sys.argv[2]), sys.argv[3])
#    elif command == 'delete':
#       delete_task(int(sys.argv[2]))
#    elif command == 'mark':
#       mark_task(int(sys.argv[2]), sys.argv[3])
#    else:
#       print('Unknown command')

# if __name__ == '__main__':
#    import sys
#    if len(sys.argv) < 2:
#       print('No command provided')
#    else:
#       command = sys.argv[1]
#       if command == 'add':
#             if len(sys.argv) < 3:
#                print('No task provided to add')
#             else:
#                add_task(sys.argv[2])
#       elif command == 'list':
#             list_tasks()
#       elif command == 'update':
#             if len(sys.argv) < 4:
#                print('Insufficient arguments for update')
#             else:
#                update_task(int(sys.argv[2]), sys.argv[3])
#       elif command == 'delete':
#             if len(sys.argv) < 3:
#                print('No task index provided to delete')
#             else:
#                delete_task(int(sys.argv[2]))
#       elif command == 'mark':
#             if len(sys.argv) < 4:
#                print('Insufficient arguments for mark')
#             else:
#                mark_task(int(sys.argv[2]), sys.argv[3])
#       else:
#             print('Unknown command')