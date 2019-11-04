"""
Day 4: String Operations and Methods
Focus: String indexing, slicing, common string methods, and formatted output.
"""

# 1. String Indexing & Slicing
message = "Python Programming"

print("--- Indexing & Slicing ---")
print(f"Full String: '{message}'")
print(f"First character (message[0]): {message[0]}")
print(f"Last character (message[-1]): {message[-1]}")
print(f"Slice [0:6]: '{message[0:6]}'")
print(f"Slice [7:]: '{message[7:]}'")
print(f"Step slicing [::2]: '{message[::2]}'")
print(f"Reversed string [::-1]: '{message[::-1]}'")

# 2. Common String Methods
raw_input_text = "   alice, engineer, python developer   "
clean_text = raw_input_text.strip()

print("\n--- String Methods ---")
print(f"Original: '{raw_input_text}'")
print(f"Stripped: '{clean_text}'")
print(f"Uppercase: '{clean_text.upper()}'")
print(f"Title Case: '{clean_text.title()}'")
print(f"Replace 'developer' with 'expert': '{clean_text.replace('developer', 'expert')}'")

# Splitting and Joining
skills = clean_text.split(", ")
print(f"Split list: {skills}")
joined_skills = " | ".join(skills)
print(f"Joined string: '{joined_skills}'")

# Inspection methods
filename = "report_2019.csv"
print(f"\nDoes '{filename}' end with '.csv'? {filename.endswith('.csv')}")
print(f"Does '{filename}' start with 'report'? {filename.startswith('report')}")

# 3. Formatting Specifiers
product = "Laptop Stand"
price = 49.956
quantity = 3
total = price * quantity

print("\n--- Formatted Output ---")
print(f"Item: {product:<15} | Qty: {quantity:>3} | Unit: ${price:>6.2f} | Total: ${total:>7.2f}")
