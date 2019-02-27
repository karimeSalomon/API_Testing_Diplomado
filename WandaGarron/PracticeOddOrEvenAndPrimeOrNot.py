def is_odd_or_even(number):
    result = 'even' if number % 2 == 0 else 'odd'
    print("This number {0} is a {1}".format(number, result))


is_odd_or_even(21)
is_odd_or_even(29)


def generate_prime_numbers(min, max):
    print("Prime numbers between {0} and {1} are: ".format(min, max))
    for num in range(min, max + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


print(generate_prime_numbers(0, 100))
