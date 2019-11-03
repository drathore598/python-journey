"""
Day 3: Operators and Expressions
Focus: Arithmetic, Comparison, Logical, Assignment, and Membership Operators.
"""

# 1. Arithmetic Operators
a = 15
b = 4

print("--- Arithmetic Operators ---")
print(f"{a} + {b} = {a + b}")    # Addition: 19
print(f"{a} - {b} = {a - b}")    # Subtraction: 11
print(f"{a} * {b} = {a * b}")    # Multiplication: 60
print(f"{a} / {b} = {a / b}")    # Float Division: 3.75
print(f"{a} // {b} = {a // b}")  # Floor Division: 3
print(f"{a} % {b} = {a % b}")    # Modulus (remainder): 3
print(f"{a} ** {b} = {a ** b}")  # Exponentiation (15^4): 50625

# 2. Comparison Operators
print("\n--- Comparison Operators ---")
x = 10
y = 20
print(f"{x} == {y} -> {x == y}")  # False
print(f"{x} != {y} -> {x != y}")  # True
print(f"{x} < {y}  -> {x < y}")   # True
print(f"{x} >= {y} -> {x >= y}")  # False

# 3. Logical Operators (and, or, not)
print("\n--- Logical Operators ---")
has_license = True
has_car = False

can_drive = has_license and has_car
can_rent = has_license or has_car
must_take_bus = not has_license

print(f"Can drive own car: {can_drive}")
print(f"Can rent or drive: {can_rent}")
print(f"Must take bus: {must_take_bus}")

# 4. Assignment & Compound Assignment Operators
print("\n--- Compound Assignment ---")
score = 100
print(f"Initial score: {score}")
score += 15  # score = score + 15
print(f"After score += 15: {score}")
score *= 2   # score = score * 2
print(f"After score *= 2: {score}")
score //= 5  # score = score // 5
print(f"After score //= 5: {score}")

# 5. Membership Operators (in, not in)
print("\n--- Membership Operators ---")
course_name = "Python 3 Fundamentals"
print(f"'Python' in course_name: {'Python' in course_name}")
print(f"'Java' not in course_name: {'Java' not in course_name}")

# Mini Exercise: Calculate body mass index (BMI)
# Formula: BMI = weight (kg) / (height (m) ** 2)
weight_kg = 70.0
height_m = 1.75
bmi = weight_kg / (height_m ** 2)
print(f"\nCalculated BMI: {bmi:.2f}")
