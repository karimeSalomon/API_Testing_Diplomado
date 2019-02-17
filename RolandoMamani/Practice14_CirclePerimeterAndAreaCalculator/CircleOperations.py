"""
Practice 14:
    - Create 1 module to Calculate the area of a circle :
                Radius * 2 * PI
    - Create 1 module to Calculate the perimeter of a circle :
                Radius * radius * PI
    - Create a script to ask to the user of the radio and print both results.
"""

import math
def calculateCircleAreaAndPerimeter():
    circle_ratio = input("Please enter the ratio value of circle:  ")
    print("Area:      " + str(calculateCircleArea(int(circle_ratio))))
    print("Perimeter: " + str(calculateCirclePerimeter(int(circle_ratio))))


def calculateCircleArea(r):
    return math.pi * r ** 2


def calculateCirclePerimeter(r):
    return math.pi*2*r


calculateCircleAreaAndPerimeter()