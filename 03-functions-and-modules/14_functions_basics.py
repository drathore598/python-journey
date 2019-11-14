"""
Day 14: Functions and Parameters
Focus: Function definitions (def), parameter types, return statements,
docstrings, and type annotations.
"""

def greet_user(name: str, greeting: str = "Hello") -> str:
    """Return a personalized greeting message.
    
    Args:
        name: Name of the person to greet.
        greeting: Greeting prefix (default is 'Hello').
    """
    return f"{greeting}, {name}!"

def convert_temperature(temp_celsius: float) -> tuple[float, float]:
    """Convert Celsius temperature into Fahrenheit and Kelvin.
    
    Returns:
        tuple containing (fahrenheit, kelvin).
    """
    fahrenheit = (temp_celsius * 9/5) + 32
    kelvin = temp_celsius + 273.15
    return round(fahrenheit, 2), round(kelvin, 2)

def is_palindrome(text: str) -> bool:
    """Check if a given string is a palindrome, ignoring spaces and case."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

print("--- Function Calls ---")
print(greet_user("Alice"))
print(greet_user("Bob", greeting="Good morning"))

# Multiple return values
f_deg, k_deg = convert_temperature(25.0)
print(f"\n25.0 C = {f_deg} F = {k_deg} K")

# Palindrome verification
test_phrases = ["Racecar", "Python", "A man a plan a canal Panama"]
print("\n--- Palindrome Checker ---")
for phrase in test_phrases:
    result = is_palindrome(phrase)
    print(f"  '{phrase}' -> Palindrome: {result}")
