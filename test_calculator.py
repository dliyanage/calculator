# test_mymath.py
import calculator
import unittest
class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calculator.subtract(1, 2)
        self.assertEqual(result, -1)


    def test_subtract_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calculator.add(1, 2)
        self.assertEqual(result, 3)


    def test_multiply_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calculator.multiply(1, 2)
        self.assertEqual(result, 2)


    def test_divide_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calculator.divide(1, 2)
        self.assertEqual(result, 0.5)

unittest.main()