# calculator.py
import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        """Divide x by y."""
        if y == 0:
           raise ValueError("Cannot divide by zero")
        return x / y

    def square_root(self, x):
        return math.sqrt(x)

    def power(self, base, exponent):
        return base ** exponent

    def factorial(self, n):
        return math.factorial(n)

    def logarithm(self, x, base):
        """Calculate the logarithm of x to the given base."""
        if x <= 0 or base <= 1:
           raise ValueError("Logarithm is not defined for these inputs")
        return math.log(x, base)
    
    def sin(self, angle):
        return math.sin(angle)

    def cos(self, angle):
        return math.cos(angle)

    def tan(self, angle):
        return math.tan(angle)
