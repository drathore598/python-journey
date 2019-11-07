"""
Day 7: While Loops
Focus: while loops, loop counters, break, continue, and while-else pattern.
"""

# 1. Basic while loop with counter
print("--- Countdown Counter ---")
counter = 5
while counter > 0:
    print(f"T-minus {counter}...")
    counter -= 1
print("Liftoff! [Success]")

# 2. Using break and continue
print("\n--- Break and Continue Example ---")
number = 0
print("Printing odd numbers below 10 (skipping even numbers, stopping at 9):")
while number < 20:
    number += 1
    if number % 2 == 0:
        continue  # skip even numbers
    if number > 9:
        break     # stop once we exceed 9
    print(f"Odd number: {number}")

# 3. Generating Fibonacci sequence up to limit
print("\n--- Fibonacci Sequence up to 100 ---")
limit = 100
a, b = 0, 1
fib_sequence = []

while a <= limit:
    fib_sequence.append(a)
    a, b = b, a + b

print(f"Fibonacci numbers <= {limit}: {fib_sequence}")

# 4. While-Else construct
# The else block executes only if the loop completed without hitting a 'break'
target = 13
current = 1
while current < 10:
    if current == target:
        print(f"Found target {target}!")
        break
    current += 1
else:
    print(f"Target {target} was NOT found within search range.")
