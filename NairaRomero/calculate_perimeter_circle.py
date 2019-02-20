"""Create 1 module to Calculate the area of a circle :
Radius * 2 * PI
Create 1 module to Calculate the perimeter of a circle :
Radius * radius * PI
Create a script to ask to the user of the radio and print both results"""
import math
def calculate_perimeter_circle(radius):
    perimeter_circle = radius * radius * math.pi
    print(perimeter_circle)
    return perimeter_circle

#calculate_perimeter_circle(3)