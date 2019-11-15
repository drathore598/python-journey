"""
Day 15: Arbitrary Arguments (*args & **kwargs)
Focus: Variable positional arguments (*args), keyword arguments (**kwargs),
and argument unpacking.
"""

def calculate_stats(*numbers: float) -> dict:
    """Accept any number of numeric arguments and return summary statistics."""
    if not numbers:
        return {"count": 0, "sum": 0, "avg": 0, "min": None, "max": None}
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "avg": round(sum(numbers) / len(numbers), 2),
        "min": min(numbers),
        "max": max(numbers)
    }

def create_user_profile(username: str, email: str, **attributes) -> dict:
    """Create a structured user profile with required fields and arbitrary metadata."""
    profile = {
        "username": username,
        "email": email,
        "metadata": attributes
    }
    return profile

def format_record(name: str, role: str, department: str) -> str:
    """Helper function to demonstrate unpacking."""
    return f"{name} is a {role} in {department}"

print("--- *args Example (Flexible Statistics) ---")
print("Stats for (10, 20, 30, 40, 50):")
print(calculate_stats(10, 20, 30, 40, 50))
print("Stats for (5, 95):")
print(calculate_stats(5, 95))

print("\n--- **kwargs Example (Flexible Profiles) ---")
user1 = create_user_profile("drathore", "drathore@example.com", plan="Pro", tier=2, city="Seattle")
print("User Profile 1:")
for k, v in user1.items():
    print(f"  {k}: {v}")

print("\n--- Argument Unpacking (* and **) ---")
params_list = ["Sarah Connor", "Security Lead", "Operations"]
print("Unpacking list with *:")
print(format_record(*params_list))

params_dict = {"name": "John Doe", "role": "Architect", "department": "Platform Engineering"}
print("Unpacking dictionary with **:")
print(format_record(**params_dict))
