import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_invalid_inputs(self):
        """Test invalid inputs for all methods."""
        with self.assertRaises(TypeError):
            self.calc.add("a", 2)
        with self.assertRaises(TypeError):
            self.calc.subtract(3, "b")
        with self.assertRaises(TypeError):
            self.calc.multiply(None, 5)
        with self.assertRaises(TypeError):
            self.calc.divide("hello", "world")

if __name__ == "__main__":
    unittest.main()
