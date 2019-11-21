"""
Day 21: Exception Handling and Custom Errors
Focus: try, except, else, finally blocks, catching specific exceptions,
and defining custom domain exceptions.
"""

# 1. Catching Specific Exceptions
def safe_divide(a: float, b: float):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero!")
        return None
    except TypeError as e:
        print(f"Type Error: {e}")
        return None
    else:
        print(f"Success: {a} / {b} = {result}")
        return result
    finally:
        print("  [Division attempt finalized]")

print("--- Safe Division Demonstrations ---")
safe_divide(20, 4)
safe_divide(15, 0)

# 2. Parsing Numeric Input Safely
def parse_positive_integer(text: str) -> int:
    try:
        val = int(text)
        if val <= 0:
            raise ValueError(f"Value must be positive, got {val}")
        return val
    except ValueError as err:
        print(f"Invalid input '{text}': {err}")
        return -1

print("\n--- Input Validation ---")
print("Parsed '42':", parse_positive_integer("42"))
print("Parsed '-5':", parse_positive_integer("-5"))
print("Parsed 'abc':", parse_positive_integer("abc"))

# 3. Custom Domain Exception
class InsufficientFundsError(Exception):
    """Raised when an account withdrawal exceeds available balance."""
    def __init__(self, balance: float, withdrawal: float):
        self.balance = balance
        self.withdrawal = withdrawal
        self.shortfall = withdrawal - balance
        super().__init__(
            f"Insufficient funds: Balance is ${balance:.2f}, attempted withdrawal ${withdrawal:.2f}. "
            f"Shortfall is ${self.shortfall:.2f}."
        )

def process_withdrawal(current_balance: float, amount: float) -> float:
    if amount > current_balance:
        raise InsufficientFundsError(current_balance, amount)
    return current_balance - amount

print("\n--- Custom Exception Handling ---")
try:
    process_withdrawal(150.0, 200.0)
except InsufficientFundsError as exc:
    print(f"Caught Custom Exception:\n  {exc}")
