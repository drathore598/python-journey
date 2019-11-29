"""
Day 29: Mini-Project - CLI Task Manager
Focus: Building a command-line application with CRUD operations,
task status tracking, and JSON persistence.
"""
import json
import os
import sys

DATA_FILE = "tasks_db.json"

class TaskManager:
    def __init__(self, storage_file: str = DATA_FILE):
        self.storage_file = storage_file
        self.tasks = self._load()

    def _load(self) -> list[dict]:
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def _save(self):
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title: str, priority: str = "Medium") -> dict:
        new_id = (max([t["id"] for t in self.tasks], default=0)) + 1
        task = {
            "id": new_id,
            "title": title,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)
        self._save()
        return task

    def complete_task(self, task_id: int) -> bool:
        for t in self.tasks:
            if t["id"] == task_id:
                t["completed"] = True
                self._save()
                return True
        return False

    def list_tasks(self):
        print(f"\n{'ID':<4} | {'Status':<10} | {'Priority':<8} | {'Title'}")
        print("-" * 55)
        for t in self.tasks:
            status = "[Done]" if t["completed"] else "[Pending]"
            print(f"{t['id']:<4} | {status:<10} | {t['priority']:<8} | {t['title']}")

def run_demo():
    print("=== CLI Task Manager Demo Mode ===")
    app = TaskManager("demo_tasks.json")
    
    # 1. Add sample tasks
    app.add_task("Complete Python OOP exercises", priority="High")
    app.add_task("Review regex pattern syntax", priority="Medium")
    app.add_task("Build capstone expense tracker", priority="High")
    app.add_task("Read documentation on itertools", priority="Low")
    
    # 2. Display initial list
    print("\nInitial Task List:")
    app.list_tasks()
    
    # 3. Mark task 1 as completed
    print("\nMarking Task 1 as completed...")
    app.complete_task(1)
    
    # 4. Display updated list
    app.list_tasks()
    
    # Clean up demo file
    if os.path.exists("demo_tasks.json"):
        os.remove("demo_tasks.json")
        print("\nDemo completed and cleaned up.")

if __name__ == "__main__":
    run_demo()
