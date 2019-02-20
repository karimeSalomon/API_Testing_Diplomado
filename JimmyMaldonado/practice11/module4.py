# Create 1 module to Calculate the perimeter of a circle :
# Radius * radius * PI

from math import pi

def calculate_circle_perimeter(radius):
    """
    Calculates the perimeter of a circle given its radius
    """
    
    perimeter = pi * radius * 2
    print("Perimeter of", radius, "is:", perimeter)

