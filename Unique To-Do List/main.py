# main.py
"""
Professional Unique To-Do List Application
Entry point of the program
Handles user interaction and menu navigation
"""

from todo_manager import TodoManager
from utils import get_valid_input

# File path for storing tasks
FILE_PATH = r"D:\Python Based Mini Project\Unique To-Do List\to-do.txt"

def main():
    # Initialize To-Do Manager with text file
    manager = TodoManager(FILE_PATH)
    
    while True:
        print("\n--- Professional Unique To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search/Filter Tasks")
        print("6. Exit")

        choice = get_valid_input("Enter choice (1-6): ", int, range(1, 7))
        
        if choice == 1:
            manager.add_task()
        elif choice == 2:
            manager.view_tasks()
        elif choice == 3:
            manager.update_task()
        elif choice == 4:
            manager.delete_task()
        elif choice == 5:
            manager.search_tasks()
        elif choice == 6:
            manager.save_data()
            print("Exiting. Your tasks are saved.")
            break

if __name__ == "__main__":
    main()
