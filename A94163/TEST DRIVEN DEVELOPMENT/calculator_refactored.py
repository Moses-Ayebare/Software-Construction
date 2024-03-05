import math

class Calculator:
    def add(self, n, j):
        """Addition operation."""
        return n + j

    def subtract(self, n, j):
        """Subtraction operation."""
        return n - j

    def multiply(self, n, j):
        """Multiplication operation."""
        return n * j

    def divide(self, n, j):
        """Division operation."""
        if j == 0:
            raise ValueError("Cannot divide by zero")
        return n / j

    def square_root(self, n):
        """Calculate the square root."""
        if n < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(n)

    def power(self, base, exponent):
        """Calculate the power of a number."""
        return math.pow(base, exponent)

    def factorial(self, n):
        """Calculate the factorial of a number."""
        if n < 0:
            raise ValueError("Cannot calculate factorial of a negative number")
        return math.factorial(n)

    def logarithm(self, n, base):
        """Calculate the logarithm of a number with a specified base."""
        if n <= 0 or base <= 1:
            raise ValueError("Invalid input for logarithm")
        return math.log(n, base)

    def sin(self, angle):
        """Calculate the sine of an angle."""
        return math.sin(angle)

    def cos(self, angle):
        """Calculate the cosine of an angle."""
        return math.cos(angle)

    def tan(self, angle):
        """Calculate the tangent of an angle."""
        return math.tan(angle)
