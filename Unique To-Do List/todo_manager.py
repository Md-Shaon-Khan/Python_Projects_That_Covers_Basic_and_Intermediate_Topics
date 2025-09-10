# todo_manager.py
"""
TodoManager Class
Handles all task operations with to-do.txt storage
"""

import json
from datetime import datetime
from utils import get_valid_input
from task_utils import is_overdue, sort_tasks

class TodoManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_data()

    def load_data(self):
        """Load tasks from text file (one JSON per line)"""
        tasks = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    task = json.loads(line.strip())
                    tasks.append(task)
        except FileNotFoundError:
            return []
        return tasks

    def save_data(self):
        """Save tasks to text file (one JSON per line)"""
        with open(self.filename, "w") as f:
            for task in self.tasks:
                f.write(json.dumps(task) + "\n")

    def add_task(self):
        """Add a new task with details and validation"""
        title = input("Enter task title: ").strip()
        if not title:
            print("Title cannot be empty.")
            return

        description = input("Enter description (optional): ").strip()
        category = input("Enter category/tag (optional): ").strip()
        priority = get_valid_input("Enter priority (Low/Medium/High): ", str, ["Low","Medium","High"])
        due_date_str = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Skipping due date.")

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "category": category,
            "priority": priority,
            "due_date": due_date,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False
        }

        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")
        self.save_data()

    def view_tasks(self):
        """Display all tasks, highlighting overdue tasks and sorting by priority"""
        if not self.tasks:
            print("No tasks available.")
            return
        
        tasks_to_show = sort_tasks(self.tasks, by="priority")
        print("\n--- Task List ---")
        for task in tasks_to_show:
            status = "Completed" if task["completed"] else "Pending"
            overdue = " [OVERDUE]" if is_overdue(task) else ""
            print(f"ID: {task['id']} | {task['title']} ({status}){overdue}")
            print(f"   Priority: {task['priority']} | Category: {task['category']} | Due: {task['due_date']}")
            print(f"   Description: {task['description']}")
            print("-"*50)

    def update_task(self):
        """Update existing task details"""
        if not self.tasks:
            print("No tasks to update.")
            return

        task_id = get_valid_input("Enter Task ID to update: ", int)
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            print("Task ID not found.")
            return

        print("Leave blank to skip updating a field.")
        title = input(f"Title ({task['title']}): ").strip()
        description = input(f"Description ({task['description']}): ").strip()
        category = input(f"Category ({task['category']}): ").strip()
        priority = input(f"Priority ({task['priority']}): ").strip()
        due_date_str = input(f"Due date ({task['due_date']}): ").strip()
        completed_str = input(f"Completed (yes/no) ({task['completed']}): ").strip()

        if title: task["title"] = title
        if description: task["description"] = description
        if category: task["category"] = category
        if priority in ["Low","Medium","High"]: task["priority"] = priority
        if due_date_str:
            try:
                task["due_date"] = datetime.strptime(due_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Skipping due date update.")
        if completed_str.lower() in ["yes","no"]:
            task["completed"] = True if completed_str.lower() == "yes" else False

        print(f"Task ID {task_id} updated successfully!")
        self.save_data()

    def delete_task(self):
        """Delete a task by ID"""
        if not self.tasks:
            print("No tasks to delete.")
            return

        task_id = get_valid_input("Enter Task ID to delete: ", int)
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            print("Task ID not found.")
            return

        self.tasks.remove(task)
        print(f"Task ID {task_id} deleted successfully!")
        self.save_data()

    def search_tasks(self):
        """Search and filter tasks by keyword, category, or priority"""
        if not self.tasks:
            print("No tasks to search.")
            return

        keyword = input("Enter keyword to search in title/description: ").strip().lower()
        category = input("Enter category to filter: ").strip().lower()
        priority = input("Enter priority to filter (Low/Medium/High): ").strip()

        filtered = self.tasks
        if keyword:
            filtered = [t for t in filtered if keyword in t["title"].lower() or keyword in t["description"].lower()]
        if category:
            filtered = [t for t in filtered if category == t["category"].lower()]
        if priority in ["Low","Medium","High"]:
            filtered = [t for t in filtered if t["priority"] == priority]

        if not filtered:
            print("No tasks found for given criteria.")
            return

        print("\n--- Search Results ---")
        for task in filtered:
            status = "Completed" if task["completed"] else "Pending"
            overdue = " [OVERDUE]" if is_overdue(task) else ""
            print(f"ID: {task['id']} | {task['title']} ({status}){overdue} | Priority: {task['priority']} | Category: {task['category']} | Due: {task['due_date']}")
