import unittest
from fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_should_return_fizz_when_value_is_3(self):
        self.assertEqual(fizzbuzz.calculate(3), "Fizz")

    def test_should_return_buzz_when_value_is_5(self):
        self.assertEqual(fizzbuzz.calculate(5), "Buzz")

    def test_should_return_the_value_when_value_is_not_3_or_5_or_divisors(self):
        self.assertEqual(fizzbuzz.calculate(1), "1")

