import math

class Calculator:
    def add(self, x, y):
        """Add two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtract y from x."""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers."""
        return x * y

    def divide(self, x, y):
        """Divide x by y."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def square_root(self, x):
        """Calculate the square root of x."""
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)

    def power(self, base, exponent):
        """Calculate base raised to the power of exponent."""
        return base ** exponent

    def factorial(self, n):
        """Calculate the factorial of a non-negative integer."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(n)

    def logarithm(self, x, base):
        """Calculate the logarithm of x to the given base."""
        if x <= 0 or base <= 1:
            raise ValueError("Logarithm is not defined for these inputs")
        return math.log(x, base)

    def sin(self, angle):
        """Calculate the sine of an angle in radians."""
        return math.sin(angle)

    def cos(self, angle):
        """Calculate the cosine of an angle in radians."""
        return math.cos(angle)

    def tan(self, angle):
        """Calculate the tangent of an angle in radians."""
        return math.tan(angle)
