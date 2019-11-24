"""
Day 24: OOP - Encapsulation and Polymorphism
Focus: Property getters and setters (@property), data validation,
and polymorphic interfaces.
"""
import math

# 1. Encapsulation with @property
class TemperatureSensor:
    def __init__(self, location: str, initial_celsius: float = 20.0):
        self.location = location
        self._celsius = initial_celsius  # Protected variable

    @property
    def celsius(self) -> float:
        """Getter for celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        """Setter with validation: physical lower bound is Absolute Zero (-273.15 C)."""
        if value < -273.15:
            raise ValueError(f"Temperature {value} C is below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Derived property computed on the fly."""
        return (self._celsius * 9 / 5) + 32


sensor = TemperatureSensor("Server Room A", 22.5)
print("--- Encapsulation with @property ---")
print(f"Location: {sensor.location}")
print(f"Reading: {sensor.celsius} C ({sensor.fahrenheit:.1f} F)")

sensor.celsius = 25.0
print(f"Updated Reading: {sensor.celsius} C ({sensor.fahrenheit:.1f} F)")

try:
    sensor.celsius = -300.0
except ValueError as err:
    print(f"Validation Error caught: {err}")

# 2. Polymorphism across different Shape classes
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


print("\n--- Polymorphism (Duck Typing) ---")
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(8, 6)
]

for s in shapes:
    # Polymorphism: Every shape implements .area() uniformly
    shape_name = s.__class__.__name__
    print(f"Shape: {shape_name:<10} | Area: {s.area():.2f}")
