def calculate(value):
    if is_divisible(value, 3) and is_divisible(value, 5):
        return 'FizzBuzz'
    elif is_divisible(value, 3):
        return 'Fizz'
    elif is_divisible(value, 5):
        return 'Buzz'

    return str(value)


def is_divisible(value, divisor):
    return value % divisor == 0
