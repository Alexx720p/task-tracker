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
        'status': 'to do',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')

def list_tasks():
    '''List all tasks'''
    tasks = load_tasks()
    for task in tasks:
        print(f"{task['id']}: {task['description']} [{task['status']}]")

def list_tasks_done():
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'done':
            print(f"{task['id']}: {task['description']} [{task['status']}]")

def list_tasks_todo():
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'to do':
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
    reassign_ids(tasks)
    save_tasks(tasks)
    print(f'Task {task_id} deleted successfully')

def reassign_ids(tasks):
    '''Reassign IDs to tasks to ensure they are sequential'''
    for index, task in enumerate(tasks):
        task['id'] = index + 1

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
                '7. Exit', )
print(*menu_options, sep='\n')

number = input('Enter the number of the task you want to perform: ')

while number != '7':
    if number == '1':
        add_task(input('Enter the task you want to add: '))
        print(*menu_options, sep='\n')

    elif number == '2':
        print('1. List all tasks',
            '2. List tasks done',
            '3. List tasks in progress',
            '4. List tasks to do',
            '5. Back to main menu', sep='\n')
        task_list_number = input('Enter the number of the list you want to perform: ')
        while task_list_number != '5':
            if task_list_number == '1':
                list_tasks()
            elif task_list_number == '2':
                list_tasks_done()
            elif task_list_number == '3':
                list_tasks_in_progress()
            elif task_list_number == '4':
                list_tasks_todo()
            else:
                print('Invalid input. Please try again.')
            task_list_number = input('Enter the number of the list you want to perform: ')
        print('Back to main menu')
        print(*menu_options, sep='\n')

    elif number == '3':
        list_tasks()
        update_task(int(
            input('Enter the task id you want to update: ')), 
            input('Enter the new task: '))
        print(*menu_options, sep='\n')
    elif number == '4':
        list_tasks()
        delete_task(int(input('Enter the task id you want to delete: ')))
        print(*menu_options, sep='\n')
    elif number == '5':
        list_tasks()
        mark_task_as_done(int(input('Enter the task id you want to mark as completed: ')), 'done')
        print(*menu_options, sep='\n')
    elif number == '6':
        list_tasks()
        mark_task_as_in_progress(int(input('Enter the task id you want to mark as in progress: ')),
                            'in progress')
        print(*menu_options, sep='\n')
    else:
        print('Invalid input. Please try again.')
        print(*menu_options, sep='\n')

    number = input('Enter the number of the task you want to perform: ')

print('Goodbye!')
