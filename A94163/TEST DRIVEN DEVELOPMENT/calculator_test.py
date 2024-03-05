import unittest
from calculator import Calculator
import math

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        # Instance of class Calculator
        self.calculator = Calculator()
    #In Python's unittest framework, test method names should start with the word "test"
    def test_add(self):
        self.assertEqual(self.calculator.adding(20, 30), 50)

    def test_subtract(self):
        self.assertEqual(self.calculator.substracting(20, 30), -10)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplying(20, 30), 600)

    def test_divide(self):
        # Test case for division operation
        self.assertEqual(self.calculator.dividing(20, 30), 20 / 30)
        # Test division by zero
        with self.assertRaises(ValueError):
            self.calculator.dividing(30, 0)


    def test_square_root(self):
        # Test case for square root operation
        self.assertEqual(self.calculator.square_root(4), 2)
        # Test case for negative input
        with self.assertRaises(ValueError):
            self.calculator.square_root(-4)

    def test_power(self):
        # Test case for power operation
        self.assertEqual(self.calculator.power(2, 3), 8)
        # Test case for zero exponent
        self.assertEqual(self.calculator.power(5, 0), 1)

    def test_factorial(self):
        # Test case for factorial operation
        self.assertEqual(self.calculator.factorial(5), 120)
        # Test case for negative input
        with self.assertRaises(ValueError):
            self.calculator.factorial(-3)

    def test_logarithm(self):
        # Test case for logarithm operation
        self.assertEqual(self.calculator.logarithm(100, 10), 2)
        # Test case for base 1
        with self.assertRaises(ValueError):
            self.calculator.logarithm(50, 1)

    def test_sin(self):
        # Test case for sine function
        self.assertAlmostEqual(self.calculator.sin(math.pi/2), 1.0, places=5)

    def test_cos(self):
        # Test case for cosine function
        self.assertAlmostEqual(self.calculator.cos(math.pi), -1.0, places=5)

    def test_tan(self):
        # Test case for tangent function
        self.assertAlmostEqual(self.calculator.tan(math.pi/4), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
