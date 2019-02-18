from math import pi


def area_of_circle(r):
    if float(r) > 10:
        return pi * r**2


print(area_of_circle(30))
print(area_of_circle(3))
