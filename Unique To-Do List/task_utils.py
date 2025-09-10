# task_utils.py
"""
Additional utilities for To-Do List Application
Includes:
- Overdue detection
- Task sorting by priority or due date
"""

from datetime import datetime

PRIORITY_ORDER = {"High": 1, "Medium": 2, "Low": 3}

def is_overdue(task):
    """
    Check if a task is overdue.
    
    Parameters:
    - task: dict, task object
    
    Returns:
    - True if overdue, False otherwise
    """
    if task.get("due_date") and not task.get("completed", False):
        due = datetime.strptime(task["due_date"], "%Y-%m-%d")
        return due < datetime.now()
    return False

def sort_tasks(tasks, by="priority"):
    """
    Sort tasks by given criteria.
    
    Parameters:
    - tasks: list of dicts
    - by: str, "priority" or "due_date"
    
    Returns:
    - sorted list of tasks
    """
    if by == "priority":
        # Sort by priority first, then by due_date (earliest first)
        return sorted(tasks, key=lambda t: (PRIORITY_ORDER.get(t.get("priority", "Low")), t.get("due_date") or "9999-12-31"))
    elif by == "due_date":
        # Sort by due date, placing tasks without due date at the end
        return sorted(tasks, key=lambda t: t.get("due_date") or "9999-12-31")
    else:
        return tasks  # No sorting if invalid option
