"""
Day 6: Conditionals and Branching
Focus: if, elif, else, nested conditions, ternary expressions, and truthy/falsy values.
"""

# 1. Basic if - elif - else
score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Student Score: {score} -> Grade: {grade}")

# 2. Ternary Operator (Conditional Expression)
age = 19
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} qualifies as: {status}")

# 3. Multiple logical conditions with boolean flags
is_member = True
purchase_total = 120.0
has_coupon = False

# Member discount rule:
# Members get 15% discount if spending over $100, or 10% otherwise.
# Non-members get 5% if spending over $100, or coupon discount if available.
if is_member:
    if purchase_total > 100:
        discount = 0.15
    else:
        discount = 0.10
else:
    if purchase_total > 100 or has_coupon:
        discount = 0.05
    else:
        discount = 0.0

final_price = purchase_total * (1 - discount)
print(f"\nOriginal Total: ${purchase_total:.2f}")
print(f"Discount Applied: {discount * 100:.0f}%")
print(f"Final Amount Due: ${final_price:.2f}")

# 4. Truthy and Falsy values in Python
empty_list = []
non_empty_str = "Python"
zero_num = 0

print("\n--- Truthy and Falsy Checks ---")
print(f"bool([]) -> {bool(empty_list)} (Empty containers are falsy)")
print(f"bool('Python') -> {bool(non_empty_str)} (Non-empty strings are truthy)")
print(f"bool(0) -> {bool(zero_num)} (Zero is falsy)")
