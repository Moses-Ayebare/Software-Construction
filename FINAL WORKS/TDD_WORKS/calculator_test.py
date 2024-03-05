# calcualtor_test.py
import unittest
from calculator import Calculator
import math

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Calculator class before each test
        self.calc = Calculator()

    def test_addition(self):
        # Test case for addition operation
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        # Test case for subtraction operation
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiplication(self):
        # Test case for multiplication operation
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_division(self):
        # Test case for division operation
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_square_root(self):
        # Test case for square root operation
        self.assertEqual(self.calc.square_root(9), 3)
        # Test case for negative input
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)

    def test_power(self):
        # Test case for power operation
        self.assertEqual(self.calc.power(2, 3), 8)
        # Test case for zero exponent
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_factorial(self):
        # Test case for factorial operation
        self.assertEqual(self.calc.factorial(5), 120)
        # Test case for negative input
        with self.assertRaises(ValueError):
            self.calc.factorial(-3)

    def test_logarithm(self):
        # Test case for logarithm operation
        self.assertEqual(self.calc.logarithm(100, 10), 2)
        # Test case for base 1
        with self.assertRaises(ValueError):
            self.calc.logarithm(50, 1)

    def test_sin(self):
        # Test case for sine function
        self.assertAlmostEqual(self.calc.sin(math.pi/2), 1.0, places=5)

    def test_cos(self):
        # Test case for cosine function
        self.assertAlmostEqual(self.calc.cos(math.pi), -1.0, places=5)

    def test_tan(self):
        # Test case for tangent function
        self.assertAlmostEqual(self.calc.tan(math.pi/4), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
