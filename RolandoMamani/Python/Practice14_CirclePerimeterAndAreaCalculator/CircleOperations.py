"""
Practice 14:
    - Create 1 module to Calculate the area of a circle :
                Radius * 2 * PI
    - Create 1 module to Calculate the perimeter of a circle :
                Radius * radius * PI
    - Create a script to ask to the user of the radio and print both results.
"""

import CircleArea as ca
import CirclePerimeter as cp

def calculateCircleAreaAndPerimeter():
    circle_ratio = input("Please enter the ratio value of circle:  ")
    print("Area:      " + str(ca.calculateCircleArea(int(circle_ratio))))
    print("Perimeter: " + str(cp.calculateCirclePerimeter(int(circle_ratio))))

calculateCircleAreaAndPerimeter()