import json
import csv

data=[
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]
with open('tasks.json', mode = 'w') as file:
    json.dump(data,file,indent=4)


def load_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)
    
def display_tasks(tasks): 
    print(f"\n{'ID':<5}{'Task Name':<20}{'Completed':<12}{'Priority'}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5}{task['task']:<20}{task['completed']:<12}{task['priority']}")
    print()

def modify_task(tasks):
    task_id = int(input("Enter the task ID to modify: "))
    for task in tasks:
        if task["id"] == task_id:
            print(f"1. Mark as completed (Current: {task['completed']})")
            print(f"2. Change priority (Current: {task['priority']})")
            choice = input("Choose an option (1/2): ")

            if choice == "1":
                task["completed"] = not task["completed"]
            elif choice == "2":
                new_priority = int(input("Enter new priority: "))
                task["priority"] = new_priority
            else:
                print("Invalid choice!")

            return tasks

    print("Task ID not found.")
    return tasks

def save_tasks(file_name, tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)
    print("Changes saved successfully.")

#Calculate Task Completion Stats

def calculate(tasks):
    total_tasks = len(tasks)
    completed_tasks = 0
    pending_tasks = 0
    average_prior = 0

    for task in tasks:
        if task['completed'] == True:
            completed_tasks+=1
        else:
            pending_tasks+=1
        average_prior += task['priority']

    average_prior = average_prior / total_tasks 
    print(f"\nTotal tasks: {total_tasks:<5} Completed tasks: {completed_tasks:<5} Pending tasks: {pending_tasks:<5} Average priority: {average_prior}")



file_name = "tasks.json"
tasks = load_json(file_name)

while True:
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Modify a Task")
    print("3. Save & Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        calculate(tasks)
        display_tasks(tasks)
    elif choice == "2":
        tasks = modify_task(tasks)
    elif choice == "3":
        save_tasks(file_name, tasks)
        break
    else:        
        print("Invalid choice, please try again.")


