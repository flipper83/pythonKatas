import unittest
from fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_should_return_fizz_when_value_is_3(self):
        self.assertEqual(fizzbuzz.calculate(3), "Fizz")

    def test_should_return_buzz_when_value_is_5(self):
        self.assertEqual(fizzbuzz.calculate(5), "Buzz")

    def test_should_return_the_value_when_value_is_not_3_or_5_or_divisors(self):
        self.assertEqual(fizzbuzz.calculate(1), "1")

    def test_should_return_fizz_when_the_value_is_divisible_by_3(self):
        self.assertEqual(fizzbuzz.calculate(9), "Fizz")

    def test_should_return_buzz_when_the_value_is_divisible_by_5(self):
        self.assertEqual(fizzbuzz.calculate(10), "Buzz")

    def test_should_return_fizzbuzz_when_the_value_is_divisible_by_3_and_5(self):
        self.assertEqual(fizzbuzz.calculate(15), "FizzBuzz")
