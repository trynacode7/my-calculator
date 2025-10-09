# small re-export so tests importing "calculator" at repo root work
from src.calculator import add, subtract, multiply, divide, power, square_root

__all__ = ["add", "subtract", "multiply", "divide", "power", "square_root"]

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with simple input validation"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """Divide a by b with zero check"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def square_root(a):
    """Calculate square root of a"""
    if not isinstance(a, (int, float)):
        raise TypeError("square_root requires a numeric input")
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5