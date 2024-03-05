import math

class Calculator:
    def adding(self, n, j):
        return n + j

    def substracting(self, n, j):
        return n - j

    def multiplying(self, n, j):
        return n * j

    def dividing(self, n, j):
        if j == 0:
            raise ValueError("Cannot divide by zero")
        return n / j

    def square_root(self, n):
        if n < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(n)

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def factorial(self, n):
        if n < 0:
            raise ValueError("Cannot calculate factorial of a negative number")
        return math.factorial(n)

    def logarithm(self, n, base):
        if n <= 0 or base <= 1:
            raise ValueError("Invalid input for logarithm")
        return math.log(n, base)

    def sin(self, angle):
        return math.sin(angle)

    def cos(self, angle):
        return math.cos(angle)

    def tan(self, angle):
        return math.tan(angle)
