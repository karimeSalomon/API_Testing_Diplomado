# Write a function area_of_circle(r) which returns the area of a circle of
# radius r only if the radius value is greater of 10.

from math import pi

def area_of_circle(radius):
    """
    Calculates the area of a circle given a radio greater than 10
    :param radius:
    :return:
    """

    if radius > 10:
        area = pi * (radius ** 2)
        print("Area of", radius, "is:", area)
    else:
        print("Radius must be greater than 10")


area_of_circle(10)

area_of_circle(15)
