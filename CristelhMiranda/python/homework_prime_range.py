
def is_prime(number):
    """Returns the True when given number is prime"""
    divisor = 0
    for current_number in range(1, number):
        if divisor >= 2:
            return False

        if number % current_number == 0:
            divisor = divisor + 1
    return True


def prime_within_range(ini, fin):
    """Prints all prime numbers within given range"""
    for number in range(ini, fin+1):
        if is_prime(number):
            print(number)


# print results
prime_within_range(2, 31)
