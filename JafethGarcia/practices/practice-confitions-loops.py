import math


def is_number(x):
    """Create 1 script to determine is a number is odd or even (use single line statement if applies)"""
    if x % 2:
        return 'odd'
    else:
        return 'even'


def is_prime(x):
    """According a list of values between a Min and Max range, identify if the number is prime or not."""
    for val in range(2, int(math.sqrt(x)) + 1):
        if not x % val:
            return False
    return True


numbers = [2, 4, 5, 7, 4, 3, 6, 9, 11, 13, 17, 18]
for num in numbers:
    print('The number', num, 'is prime?', is_prime(num), 'and is also', is_number(num))
