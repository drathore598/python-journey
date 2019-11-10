"""
Day 10: Tuples and Immutability
Focus: Tuple creation, immutability, packing and unpacking, and use cases.
"""

# 1. Creating Tuples
coordinates = (37.7749, -122.4194)  # San Francisco lat/lon
single_element_tuple = (42,)         # Trailing comma required for 1-element tuple

print(f"Coordinates: {coordinates}")
print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
print(f"Type: {type(coordinates)}")

# 2. Immutability Concept
# Tuples cannot be modified after creation:
# coordinates[0] = 38.0 -> Raises TypeError: 'tuple' object does not support item assignment
print("\nTuples protect fixed records from accidental modification.")

# 3. Tuple Packing and Unpacking
point = 10, 20, 30  # Packing without parentheses
x, y, z = point     # Unpacking
print(f"\nPacked point: {point}")
print(f"Unpacked: x={x}, y={y}, z={z}")

# Swapping variables without temporary storage
first = "A"
second = "B"
print(f"Before swap: first={first}, second={second}")
first, second = second, first
print(f"After swap:  first={first}, second={second}")

# 4. Tuple Methods (.count and .index)
grades = ("A", "B", "A", "C", "A", "B")
print(f"\nGrades tuple: {grades}")
print(f"Count of 'A': {grades.count('A')}")
print(f"First index of 'C': {grades.index('C')}")

# 5. Returning Multiple Values from a Function
def min_max_avg(numbers_list):
    """Returns minimum, maximum, and average as a tuple."""
    return min(numbers_list), max(numbers_list), sum(numbers_list) / len(numbers_list)

stats = min_max_avg([10, 25, 40, 55, 70])
minimum, maximum, average = stats
print(f"\nStatistics tuple: {stats}")
print(f"Min: {minimum}, Max: {maximum}, Avg: {average:.2f}")
