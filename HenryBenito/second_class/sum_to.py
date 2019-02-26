def sum_to(number):
    result = 0
    if int(number) > 35:
        number = 35
    for value in range(1, int(number) + 1):
        result += value
    return result


print(sum_to(10))
print(sum_to(35))
print(sum_to(250))
