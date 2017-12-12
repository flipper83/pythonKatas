def calculate(value):
    if is_disivible(value, 3) and is_disivible(value, 5):
        return 'FizzBuzz'
    elif is_disivible(value, 3):
        return 'Fizz'
    elif is_disivible(value, 5):
        return 'Buzz'

    return str(value)


def is_disivible(value, divisor):
    return value % divisor == 0
