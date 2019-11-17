"""
Day 17: Variable Scope and Closures
Focus: LEGB scope resolution, global and nonlocal keywords,
and function closures.
"""

# 1. Global vs Local Scope
app_name = "JourneyApp"  # Global scope

def show_scope_demo():
    version = "1.0.0"     # Local scope
    print(f"Inside function: app_name='{app_name}', version='{version}'")

show_scope_demo()

# 2. Modifying Global Variables (global keyword)
counter = 0

def increment_global():
    global counter
    counter += 1

increment_global()
increment_global()
print(f"Global counter after 2 increments: {counter}")

# 3. Nested Functions and nonlocal keyword
def make_accumulator(initial_value: int = 0):
    """Factory function returning a stateful closure using nonlocal."""
    total = initial_value

    def add(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return add

acc1 = make_accumulator(100)
print("\n--- Closure (Accumulator 1) ---")
print(f"Add 25: {acc1(25)}")  # 125
print(f"Add 50: {acc1(50)}")  # 175

acc2 = make_accumulator(0)
print("\n--- Closure (Accumulator 2 - Independent state) ---")
print(f"Add 10: {acc2(10)}")  # 10
print(f"Add 5:  {acc2(5)}")   # 15

# 4. Multiplier Closure
def make_multiplier(factor: float):
    return lambda x: x * factor

double = make_multiplier(2)
triple = make_multiplier(3)

print("\n--- Multiplier Closures ---")
print(f"double(14): {double(14)}")
print(f"triple(14): {triple(14)}")
