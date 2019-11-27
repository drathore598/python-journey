"""
Day 27: Decorators and Function Wrappers
Focus: Higher-order functions, custom decorators (@timer, @logger),
and preserving function metadata with functools.wraps.
"""
import time
import functools

# 1. Timing Decorator
def execution_timer(func):
    """Decorator that measures and prints execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"[TIMER] '{func.__name__}' executed in {elapsed * 1000:.3f} ms")
        return result
    return wrapper

# 2. Logging Decorator
def call_logger(func):
    """Decorator that logs input arguments and return value."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join(repr(a) for a in args)
        print(f"[CALL] {func.__name__}({arg_str})")
        result = func(*args, **kwargs)
        print(f"[RETURN] {func.__name__} -> {result}")
        return result
    return wrapper

# 3. Applying Decorators
@execution_timer
@call_logger
def compute_sum_of_squares(limit: int) -> int:
    """Compute sum of squares from 1 to limit."""
    return sum(i ** 2 for i in range(1, limit + 1))

print("--- Applying Chained Decorators ---")
total = compute_sum_of_squares(5000)
print(f"Result: {total}")
print(f"Preserved Docstring: '{compute_sum_of_squares.__doc__}'")
print(f"Preserved Function Name: '{compute_sum_of_squares.__name__}'")

# 4. Decorator with Arguments
def repeat_call(times: int):
    """Decorator factory that repeats function execution N times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_result = None
            for i in range(times):
                last_result = func(*args, **kwargs)
            return last_result
        return wrapper
    return decorator

@repeat_call(times=3)
def ping(server_name: str):
    print(f"Pinging {server_name}... Pong!")

print("\n--- Parameterized Decorator (@repeat_call(3)) ---")
ping("api.internal.network")
