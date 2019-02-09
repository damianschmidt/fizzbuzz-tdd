import unittest
import fizzbuzz
from parameterized import parameterized


class TestFizzBuzz(unittest.TestCase):
    @parameterized.expand([[3], [12], [36]])
    def test_return_fizz(self, value):
        """ Should return Fizz when number is divisible by three """
        result = fizzbuzz.check(value)
        self.assertEqual("Fizz", result)

    @parameterized.expand([[5], [10], [20]])
    def test_return_buzz(self, value):
        """ Should return Buzz when number is divisible by five """
        result = fizzbuzz.check(value)
        self.assertEqual("Buzz", result)

    @parameterized.expand([[15], [45], [300]])
    def test_return_fizzbuzz(self, value):
        """ Should return FizzBuzz when number is divisible by three and five """
        result = fizzbuzz.check(value)
        self.assertEqual("FizzBuzz", result)

    @parameterized.expand([[2], [7], [19]])
    def test_return_number(self, value):
        """ Should return number when number is not divisible by three or five """
        result = fizzbuzz.check(value)
        self.assertEqual(str(value), result)
