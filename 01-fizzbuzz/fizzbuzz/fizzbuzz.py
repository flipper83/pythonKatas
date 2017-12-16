def calculate(value):
    if (is_divisible(value, 3) and is_divisible(value, 5)) \
            or (contains(value, '3') and contains(value, '5')):
        return 'FizzBuzz'
    elif is_divisible(value, 3) or contains(value, '3'):
        return 'Fizz'
    elif is_divisible(value, 5) or contains(value, '5'):
        return 'Buzz'

    return str(value)


def is_divisible(value, divisor):
    return value % divisor == 0


def contains(value, number):
    return str(value).__contains__(number)
