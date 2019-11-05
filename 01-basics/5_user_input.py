"""
Day 5: User Input and Type Casting
Focus: input(), type conversions (str to int/float), handling inputs safely,
and building a tip & split calculator.
"""
import sys

def get_input(prompt_text, default_value):
    """Utility to allow interactive input or fallback to default during automated runs."""
    if sys.stdin.isatty():
        val = input(prompt_text)
        return val if val.strip() != "" else default_value
    return default_value

print("--- User Input & Type Casting Demonstration ---")

# Type conversion basics
user_name = get_input("Enter your name [Default: Taylor]: ", "Taylor")
birth_year_str = get_input("Enter birth year [Default: 1995]: ", "1995")

# Type casting str to int
birth_year = int(birth_year_str)
current_year = 2019
calculated_age = current_year - birth_year

print(f"Hello, {user_name}! In {current_year}, you will turn approximately {calculated_age} years old.")

# Mini-Project: Restaurant Bill Split Calculator
print("\n--- Restaurant Bill & Tip Calculator ---")
bill_str = get_input("Enter total bill amount ($) [Default: 124.50]: ", "124.50")
tip_percent_str = get_input("Enter tip percentage (e.g. 15, 18, 20) [Default: 18]: ", "18")
people_count_str = get_input("Number of people splitting [Default: 4]: ", "4")

bill_amount = float(bill_str)
tip_percent = float(tip_percent_str)
people_count = int(people_count_str)

tip_amount = bill_amount * (tip_percent / 100)
total_amount = bill_amount + tip_amount
share_per_person = total_amount / people_count

print("\n--- Bill Summary ---")
print(f"Subtotal:       ${bill_amount:.2f}")
print(f"Tip ({tip_percent:.0f}%):     ${tip_amount:.2f}")
print(f"Total:          ${total_amount:.2f}")
print(f"Split ({people_count} ways): ${share_per_person:.2f} per person")
