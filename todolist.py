import os
import json

class TodoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        """Add a new task."""
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def remove_task(self, task_id):
        """Remove a task by its ID."""
        if 0 <= task_id < len(self.tasks):
            del self.tasks[task_id]
            self.save_tasks()

    def mark_task_complete(self, task_id):
        """Mark a task as completed."""
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]['completed'] = True
            self.save_tasks()

    def list_tasks(self):
        """List  all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks):
                status = 'Completed' if task['completed'] else 'Pending'
                print(f"{index + 1}. {task['task']} - {status}")

    def run(self):
        """  main menu ."""
        while True:
            print("\n--- To-Do List ---")
            print("1. List tasks")
            print("2. Add a task")
            print("3. Remove a task")
            print("4. Mark task as completed")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.list_tasks()
            elif choice == '2':
                task = input("Enter the task description: ")
                self.add_task(task)
            elif choice == '3':
                self.list_tasks()
                task_id = int(input("Enter the task number to remove: ")) - 1
                self.remove_task(task_id)
            elif choice == '4':
                self.list_tasks()
                task_id = int(input("Enter the task number to mark as completed: ")) - 1
                self.mark_task_complete(task_id)
            elif choice == '5':
                print("Exiting the To-Do List app. Thanks for using the application ,Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Running the application
if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.run()
