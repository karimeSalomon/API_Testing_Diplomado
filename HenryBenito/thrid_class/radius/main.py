import area
import perimeter
from math import pi


radius = float(input("Enter radius: "))
print("Area is: {}".format(area.calculate(radius, pi)))
print("Perimeter is: {}".format(perimeter.calculate(radius, pi)))
