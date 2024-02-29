import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def square_root(self, x):
        return math.sqrt(x)

    def power(self, base, exponent):
        return base ** exponent

    def factorial(self, n):
        return math.factorial(n)

    def logarithm(self, x, base):
        return math.log(x, base)
    
    def sin(self, angle):
        return math.sin(angle)

    def cos(self, angle):
        return math.cos(angle)

    def tan(self, angle):
        return math.tan(angle)
