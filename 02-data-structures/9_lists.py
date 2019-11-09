"""
Day 9: Lists and List Operations
Focus: List creation, indexing, mutating methods, sorting, and slicing operations.
"""

# 1. Creating and Accessing Lists
fruits = ["apple", "banana", "cherry", "date"]
print(f"Initial list: {fruits}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# 2. Modifying Lists (Adding and Removing items)
print("\n--- Modifying Lists ---")
fruits.append("elderberry")       # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")      # Insert at index 1
print(f"After insert at 1: {fruits}")

fruits.extend(["fig", "grape"])    # Extend with multiple items
print(f"After extend: {fruits}")

removed_item = fruits.pop()        # Remove last item
print(f"Popped item: '{removed_item}' | List: {fruits}")

fruits.remove("banana")            # Remove first occurrence
print(f"After removing 'banana': {fruits}")

# 3. Sorting and Reversing
numbers = [42, 17, 89, 5, 23, 67]
print(f"\nOriginal numbers: {numbers}")

# sorted() creates a new list; .sort() sorts in-place
sorted_numbers = sorted(numbers)
print(f"sorted() copy: {sorted_numbers}")
print(f"Original untouched: {numbers}")

numbers.sort(reverse=True)
print(f"In-place sorted (descending): {numbers}")

# 4. List Statistics & Utility Functions
print(f"\nMin: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")
print(f"Contains 42? {42 in numbers}")
print(f"Length of list: {len(numbers)}")
