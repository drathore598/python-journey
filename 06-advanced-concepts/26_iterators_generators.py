"""
Day 26: Iterators and Generator Functions
Focus: Iterator protocol (__iter__, __next__), generator functions with yield,
and memory-efficient streams.
"""
import sys

# 1. Custom Iterator implementing the Iterator Protocol
class StepCountdown:
    """Custom iterator counting down from start to zero with a step."""
    def __init__(self, start: int, step: int = 1):
        self.current = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= self.step
        return val

print("--- Custom Iterator ---")
countdown = StepCountdown(10, step=2)
for val in countdown:
    print(f"Count: {val}")

# 2. Generator Function with yield
def fibonacci_generator(count: int):
    """Yield first 'count' Fibonacci numbers on-demand."""
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

print("\n--- Fibonacci Generator ---")
fib_gen = fibonacci_generator(8)
print("Type of fib_gen:", type(fib_gen))
print("Values from generator:", list(fib_gen))

# 3. Memory efficiency: List vs Generator expression
n_items = 100_000

list_comp = [x ** 2 for x in range(n_items)]
gen_exp = (x ** 2 for x in range(n_items))

size_list_bytes = sys.getsizeof(list_comp)
size_gen_bytes = sys.getsizeof(gen_exp)

print("\n--- Memory Comparison (100,000 items) ---")
print(f"List comprehension memory: {size_list_bytes:,} bytes")
print(f"Generator expression memory: {size_gen_bytes:,} bytes")
print(f"Memory reduction factor: {size_list_bytes // size_gen_bytes}x less memory!")
