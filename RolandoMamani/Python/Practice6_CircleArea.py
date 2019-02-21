"""
Practice 6:  Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is greater of 10.
"""

import math

def area_of_circle(r):
    if(r > 10):
        print("The area of circle with radio of " + str(r) + " is:  " + str(math.pi * (r**2)))
    else:
        print("Invalid number, you should enter a number higher than 10. I.e. from 11 onwards")

area_of_circle(int(input("Enter the ratio of circle which should be from 11 onwards: ")))