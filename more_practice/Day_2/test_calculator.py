import unittest
from Day_2 import calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = calculator.Calculator()

    def test_addition(self):
        # calc = calculator.Calculator()
        result = self.calc.a + self.calc.b

        self.assertEqual(self.calc.add(), result)

    def test_subtraction(self):
        # calc = calculator.Calculator()
        result = self.calc.a - self.calc.b

        self.assertEqual(self.calc.sub(), result)

    def test_multiplication(self):
        # calc = calculator.Calculator()
        result = self.calc.a * self.calc.b
        self.assertEqual(self.calc.mul(), result)

    def test_division(self):
        # calc = calculator.Calculator()
        if self.calc.b == 0:
            result = None
            self.assertEqual(self.calc.div(), result)
        else:
            result = self.calc.a / self.calc.b
            self.assertEqual(self.calc.div(), result)

