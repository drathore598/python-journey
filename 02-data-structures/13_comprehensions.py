"""
Day 13: List, Dict, and Set Comprehensions
Focus: Concise transformations, conditional filtering, and nested comprehensions.
"""

# 1. List Comprehensions: Mapping and Filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares of even numbers
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("--- List Comprehensions ---")
print(f"Original numbers: {numbers}")
print(f"Even squares: {even_squares}")

# Transforming strings: clean and normalize emails
emails = [" ALICE@Example.COM ", "bob@work.ORG  ", "  charlie@DOMAIN.NET "]
cleaned_emails = [e.strip().lower() for e in emails]
print(f"\nCleaned emails: {cleaned_emails}")

# 2. Dictionary Comprehensions
item_prices = {"apple": 0.50, "milk": 2.20, "bread": 1.75, "cheese": 4.50}

# Price with 10% tax added
taxed_prices = {item: round(price * 1.10, 2) for item, price in item_prices.items()}
print("\n--- Dictionary Comprehensions ---")
print(f"Original prices: {item_prices}")
print(f"Taxed prices (+10%): {taxed_prices}")

# Filtering dictionary entries
expensive_items = {item: price for item, price in item_prices.items() if price > 2.0}
print(f"Items > $2.00: {expensive_items}")

# 3. Set Comprehensions
words = ["apple", "banana", "Avocado", "cherry", "apricot", "Berry"]
# Unique first letters lowercased
first_letters = {w[0].lower() for w in words}
print("\n--- Set Comprehensions ---")
print(f"Unique starting letters: {sorted(first_letters)}")

# 4. Nested List Comprehension (Matrix Flattening)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [val for row in matrix for val in row]
print(f"\nMatrix: {matrix}")
print(f"Flattened list: {flattened}")
