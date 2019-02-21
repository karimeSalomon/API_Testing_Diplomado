# Create 1 module to Calculate the area of a circle :
# Radius * 2 * PI
# 
# Create 1 module to Calculate the perimeter of a circle :
# Radius * radius * PI
# 
# Create a script to ask to the user of the radio and print both results.

import module3
import module4

def main():
    """
    Calculates the area and perimeter of a circle given its radius
    """

    radius = int(input("Enter the radius: "))

    module3.calculate_circle_area(radius)
    module4.calculate_circle_perimeter(radius)


main()