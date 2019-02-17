# Write a function sum_to(n) that returns the sum of all integer numbers
# up to and including only until any value lower than 35. So
# sum_to(10)wouldbe1+2+3...+10which would return the value 55, but if
# n=40 only until sum to 35 need to be returned.

def sum_to(number):
    """
    Prints the sum of all integer numbers given a limit
    :param number:
    :return:
    """
    sum = 0
    for i in range(1, number + 1):
        if i < 35:
            sum += i
        else:
            print("Limit has been reached")
            break
    print("Sum of", number, "is:", sum)


sum_to(10)

sum_to(35)

sum_to(40)