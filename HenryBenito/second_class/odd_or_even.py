import math


def odd_or_even(number):
    return "{} is odd".format(number) if int(number) % 2 == 0 else "{} is even".format(number)


def is_prime(number):
    if 0 < int(number) < 2:
        return True
    for number_to_try in range(2, int(math.sqrt(int(number))) + 1):
        if number % number_to_try == 0:
            return False
    return True


def list_a_range(min, max):
    for value in range(min, max):
        print(odd_or_even(value))
        print("is prime?: {}".format(is_prime(value)))


list_a_range(2, 30)
