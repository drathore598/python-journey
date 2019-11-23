"""
Day 23: OOP - Inheritance and Method Overriding
Focus: Base and derived classes, super(), overriding methods,
and isinstance/issubclass checks.
"""

class Employee:
    """Base class representing an organization employee."""
    def __init__(self, emp_id: int, name: str, base_salary: float):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self) -> float:
        """Base salary computation."""
        return self.base_salary

    def get_details(self) -> str:
        return f"[{self.emp_id}] {self.name} | Role: General Employee | Pay: ${self.calculate_pay():.2f}"


class Developer(Employee):
    """Derived class representing a software developer with bonus skills."""
    def __init__(self, emp_id: int, name: str, base_salary: float, tech_stack: list[str]):
        super().__init__(emp_id, name, base_salary)
        self.tech_stack = tech_stack

    def calculate_pay(self) -> float:
        # Developers receive a 10% performance bonus
        return self.base_salary * 1.10

    def get_details(self) -> str:
        skills = ", ".join(self.tech_stack)
        return f"[{self.emp_id}] {self.name} | Role: Developer ({skills}) | Pay: ${self.calculate_pay():.2f}"


class Manager(Employee):
    """Derived class representing a team manager with managed reports."""
    def __init__(self, emp_id: int, name: str, base_salary: float, team_size: int):
        super().__init__(emp_id, name, base_salary)
        self.team_size = team_size

    def calculate_pay(self) -> float:
        # Managers receive $150 bonus per team member
        return self.base_salary + (self.team_size * 150.0)

    def get_details(self) -> str:
        return f"[{self.emp_id}] {self.name} | Role: Manager (Team: {self.team_size}) | Pay: ${self.calculate_pay():.2f}"


print("--- Employee Hierarchy ---")
staff = [
    Employee(101, "Morgan Vance", 50000.0),
    Developer(102, "Alex Chen", 75000.0, ["Python", "Docker", "PostgreSQL"]),
    Manager(103, "Samantha Ross", 85000.0, team_size=6)
]

for person in staff:
    print(person.get_details())

# Type inspection
dev = staff[1]
print(f"\nIs dev an instance of Developer? {isinstance(dev, Developer)}")
print(f"Is dev an instance of Employee?  {isinstance(dev, Employee)}")
print(f"Is Manager a subclass of Employee? {issubclass(Manager, Employee)}")
