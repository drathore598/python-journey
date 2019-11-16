"""
Day 16: Lambda Functions and Built-in Utilities
Focus: Anonymous functions (lambda), map(), filter(), custom sorting keys,
and any() / all() assertions.
"""

# 1. Lambda Expressions
square = lambda x: x ** 2
add = lambda a, b: a + b
print("--- Basic Lambdas ---")
print(f"square(6): {square(6)}")
print(f"add(7, 8): {add(7, 8)}")

# 2. Using map() and filter()
raw_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, raw_numbers))
# Map: multiply each filtered number by 10
scaled_evens = list(map(lambda x: x * 10, evens))

print("\n--- map() and filter() Pipeline ---")
print(f"Raw numbers:    {raw_numbers}")
print(f"Filtered evens: {evens}")
print(f"Scaled evens:   {scaled_evens}")

# 3. Sorting with custom lambda key
inventory = [
    {"product": "Keyboard", "price": 85.00, "stock": 14},
    {"product": "Mouse", "price": 32.50, "stock": 45},
    {"product": "Monitor", "price": 280.00, "stock": 8},
    {"product": "USB Hub", "price": 19.99, "stock": 60}
]

# Sort by price ascending
by_price = sorted(inventory, key=lambda item: item["price"])
print("\n--- Sorted by Price (Ascending) ---")
for item in by_price:
    print(f"  {item['product']:<12}: ${item['price']:>6.2f} (Stock: {item['stock']})")

# 4. any() and all()
temperatures = [22, 24, 19, 21, 26, 23]
has_freezing = any(t <= 0 for t in temperatures)
all_comfortable = all(18 <= t <= 28 for t in temperatures)

print("\n--- Any / All Assertions ---")
print(f"Temperatures: {temperatures}")
print(f"Any freezing (<= 0)? {has_freezing}")
print(f"All comfortable (18..28)? {all_comfortable}")
