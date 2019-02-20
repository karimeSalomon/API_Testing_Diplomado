# Create 1 script to determine is a number is
# odd or even (use single line statement if
# applies).

def is_odd_or_even(number):
    """
    Prints if a given number is odd or even
    :param number:
    :return:
    """

    if number % 2 == 0: print(number, " is odd")
    else: print(number, "is even")


is_odd_or_even(10)

is_odd_or_even(7)