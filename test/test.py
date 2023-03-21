import unittest

from alleygator import sum

class TestSum(unittest.TestCase):
    def test_sum_adds_to_numbers(self):
        """
        Sum should be able to just add two numbers.
        """
        self.assertEqual(sum(1, 1), 2)

if __name__ == "__main__":
    unittest.main()