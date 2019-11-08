"""
Day 8: For Loops and Iteration
Focus: for loops, range() variations, enumerate(), zip(), and nested iterations.
"""

# 1. Range variations: range(stop), range(start, stop), range(start, stop, step)
print("--- Range Variations ---")
print("range(5):", list(range(5)))
print("range(2, 8):", list(range(2, 8)))
print("range(10, 0, -2):", list(range(10, 0, -2)))

# 2. Iterating through a collection with enumerate()
languages = ["Python", "JavaScript", "Rust", "Go"]
print("\n--- Enumerate (Index + Element) ---")
for index, lang in enumerate(languages, start=1):
    print(f"{index}. {lang}")

# 3. Parallel iteration with zip()
students = ["Emma", "Liam", "Sophia", "Noah"]
scores = [92, 85, 98, 88]

print("\n--- Paired Iteration with zip() ---")
for name, score in zip(students, scores):
    print(f"Student: {name:<8} -> Score: {score}")

# 4. Nested loops: Multiplication Table (1 through 5)
print("\n--- Nested Loop: 5x5 Grid ---")
for row in range(1, 6):
    row_values = []
    for col in range(1, 6):
        row_values.append(f"{row * col:3d}")
    print(" ".join(row_values))

# 5. Accumulator pattern
numbers = [12, 45, 68, 23, 91, 34]
total_sum = 0
for num in numbers:
    total_sum += num
average = total_sum / len(numbers)
print(f"\nNumbers: {numbers}")
print(f"Sum: {total_sum}, Average: {average:.2f}")
