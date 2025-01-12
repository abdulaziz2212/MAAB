import os
import json
import csv

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "Task ID": self.task_id,
            "Title": self.title,
            "Description": self.description,
            "Due Date": self.due_date,
            "Status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(data["Task ID"], data["Title"], data["Description"], data["Due Date"], data["Status"])

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class StorageInterface:
    def save(self, tasks):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


class CSVStorage(StorageInterface):
    def __init__(self, file_name="tasks.csv"):
        self.file_name = file_name

    def save(self, tasks):
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Task ID", "Title", "Description", "Due Date", "Status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file)
            return [Task.from_dict(row) for row in reader]


class JSONStorage(StorageInterface):
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name

    def save(self, tasks):
        with open(self.file_name, "w") as file:
            json.dump([task.to_dict() for task in tasks], file)

    def load(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r") as file:
            return [Task.from_dict(task) for task in json.load(file)]


class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task_id, title, description, due_date, status):
        new_task = Task(task_id, title, description, due_date, status)
        self.tasks.append(new_task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print(f"Task with ID {task_id} updated.")
                return
        print(f"No task with ID {task_id} found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print(f"Task with ID {task_id} deleted.")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered_tasks:
            print("No tasks found with the given status.")
        else:
            for task in filtered_tasks:
                print(task)

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully.")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded successfully.")


def main():
    print("Choose storage format:")
    print("1. CSV")
    print("2. JSON")
    choice = input("Enter your choice: ")

    storage = CSVStorage() if choice == "1" else JSONStorage()

    manager = TaskManager(storage)

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            manager.add_task(task_id, title, description, due_date, status)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep current): ")
            description = input("Enter new Description (leave blank to keep current): ")
            due_date = input("Enter new Due Date (leave blank to keep current): ")
            status = input("Enter new Status (leave blank to keep current): ")
            manager.update_task(task_id, title, description, due_date, status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter by: ")
            manager.filter_tasks(status)
        elif choice == "6":
            manager.save_tasks()
        elif choice == "7":
            manager.load_tasks()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
