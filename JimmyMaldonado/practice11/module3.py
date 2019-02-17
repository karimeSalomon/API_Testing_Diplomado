# Create 1 module to Calculate the area of a circle :
# Radius * 2 * PI

from math import pi

def calculate_circle_area(radius):
    """
    Calculates the area of a circle given its radius
    """
    
    area = pi * (radius ** 2)
    print("Area of", radius, "is:", area)