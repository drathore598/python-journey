"""
Day 18: Modules, Packages, and Standard Library
Focus: Importing standard library tools (math, random, datetime, collections),
and importing custom modules.
"""
import math
import random
import datetime
from collections import Counter

# Import our custom helper module
from math_utils import is_prime, circle_area

# 1. Standard Library: math & random
print("--- Standard Library: math & random ---")
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"sin({angle_deg} deg): {math.sin(angle_rad):.4f}")
print(f"Factorial of 6: {math.factorial(6)}")

random.seed(42)  # Deterministic seed for reproducible testing
dice_rolls = [random.randint(1, 6) for _ in range(10)]
print(f"10 Simulated dice rolls: {dice_rolls}")

# 2. Standard Library: datetime
print("\n--- Standard Library: datetime ---")
today = datetime.date(2019, 11, 18)
two_weeks_later = today + datetime.timedelta(days=14)
print(f"Study session date: {today.strftime('%A, %B %d, %Y')}")
print(f"Target milestone date: {two_weeks_later.strftime('%A, %B %d, %Y')}")

# 3. Standard Library: collections.Counter
print("\n--- collections.Counter ---")
votes = ["Python", "Rust", "Python", "Go", "Python", "Rust", "JavaScript"]
vote_counts = Counter(votes)
print(f"Votes summary: {vote_counts}")
print(f"Most popular: {vote_counts.most_common(1)[0]}")

# 4. Using Custom Module
print("\n--- Custom Module (math_utils) ---")
test_numbers = [2, 7, 10, 13, 29, 35, 41]
prime_results = {n: is_prime(n) for n in test_numbers}
print(f"Prime checks: {prime_results}")
print(f"Circle area (r=4.5): {circle_area(4.5):.2f}")
