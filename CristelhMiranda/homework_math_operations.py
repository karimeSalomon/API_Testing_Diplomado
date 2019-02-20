import math


def area_of_circle(r):
    if r > 10:
        return math.pi * r * r


def sum_to(n):
    top_range = (n+1) if (n <= 35) else 36
    result = 0
    for num in range(top_range):
        result = result + num
    return result


# Call area_of_circle(r)
print(area_of_circle(2))
print(area_of_circle(11))

# Call sum_to
print(sum_to(10))
print(sum_to(35))
print(sum_to(40))
