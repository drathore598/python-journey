"""
Day 30: Capstone Project - Personal Expense Tracker
Focus: Comprehensive project integrating OOP, JSON persistence,
category analytics, budget alerts, and formatted reporting.
"""
import json
import os
from datetime import datetime

class Expense:
    """Represents an individual expense transaction."""
    def __init__(self, expense_id: int, date_str: str, category: str, amount: float, description: str):
        self.expense_id = expense_id
        self.date_str = date_str
        self.category = category
        self.amount = float(amount)
        self.description = description

    def to_dict(self) -> dict:
        return {
            "id": self.expense_id,
            "date": self.date_str,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["date"], data["category"], data["amount"], data["description"])


class ExpenseTracker:
    """Manages expense transactions, category analytics, and budget reports."""
    def __init__(self, monthly_budget: float = 1000.0, storage_file: str = "expenses.json"):
        self.monthly_budget = monthly_budget
        self.storage_file = storage_file
        self.expenses: list[Expense] = []
        self._load()

    def _load(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)
                    self.expenses = [Expense.from_dict(d) for d in raw_data]
            except Exception:
                self.expenses = []

    def _save(self):
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=2)

    def add_expense(self, date_str: str, category: str, amount: float, description: str) -> Expense:
        new_id = (max([e.expense_id for e in self.expenses], default=0)) + 1
        expense = Expense(new_id, date_str, category, amount, description)
        self.expenses.append(expense)
        self._save()
        return expense

    def total_spending(self) -> float:
        return sum(e.amount for e in self.expenses)

    def spending_by_category(self) -> dict[str, float]:
        summary = {}
        for e in self.expenses:
            summary[e.category] = round(summary.get(e.category, 0.0) + e.amount, 2)
        return summary

    def generate_report(self):
        total = self.total_spending()
        cat_summary = self.spending_by_category()
        remaining_budget = self.monthly_budget - total
        
        print("=" * 60)
        print("         PERSONAL EXPENSE TRACKER - MONTHLY REPORT         ")
        print("=" * 60)
        print(f"Monthly Budget:   ${self.monthly_budget:>9.2f}")
        print(f"Total Spent:      ${total:>9.2f}")
        print(f"Remaining:        ${remaining_budget:>9.2f}")
        
        if total > self.monthly_budget:
            print("ALERT: Monthly budget exceeded!")
        else:
            print("Status: Within healthy spending limits.")

        print("\n--- Breakdown by Category ---")
        for cat, amt in sorted(cat_summary.items(), key=lambda x: x[1], reverse=True):
            pct = (amt / total * 100) if total > 0 else 0
            bar = "#" * int(pct // 5)
            print(f"  {cat:<14}: ${amt:>7.2f} ({pct:>5.1f}%) | {bar}")

        print("\n--- Recent Transactions ---")
        print(f"{'ID':<4} | {'Date':<10} | {'Category':<12} | {'Amount':<8} | {'Description'}")
        print("-" * 60)
        for e in self.expenses[-5:]:
            print(f"{e.expense_id:<4} | {e.date_str:<10} | {e.category:<12} | ${e.amount:>7.2f} | {e.description}")
        print("=" * 60)


def main():
    test_db = "capstone_expenses_demo.json"
    tracker = ExpenseTracker(monthly_budget=800.0, storage_file=test_db)
    
    # Seed representative monthly expenses
    tracker.add_expense("2019-11-04", "Education", 49.99, "Python Course Materials")
    tracker.add_expense("2019-11-09", "Groceries", 85.50, "Weekly grocery essentials")
    tracker.add_expense("2019-11-15", "Utilities", 65.00, "Internet service bill")
    tracker.add_expense("2019-11-20", "Dining", 38.25, "Lunch with study group")
    tracker.add_expense("2019-11-25", "Groceries", 92.40, "Supermarket shopping")
    tracker.add_expense("2019-11-28", "Tech", 120.00, "Mechanical keyboard")
    
    tracker.generate_report()
    
    # Cleanup demo database
    if os.path.exists(test_db):
        os.remove(test_db)

if __name__ == "__main__":
    main()
