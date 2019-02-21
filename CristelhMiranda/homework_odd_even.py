def is_even_or_odd(number):
    if number % 2 == 0:
        message = "is even"
    else:
        message = "is odd"
    print(f"{number} {message}")


# print results
is_even_or_odd(2)
is_even_or_odd(3)

