def is_prime(num):
    for n in range(2, num):
        if number % n == 0:
            return False

    return True


numbers = [1, 2, 3, 7, 10]

for number in numbers:
    print(is_prime(number))
