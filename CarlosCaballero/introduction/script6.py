# practice #4

# write a function area_of_circle(r) which returns the area of a circle of
# radius r only if the radius value is greater of 10.

import math
import sys

def area_of_circle(r):
    return math.pi * r * r

# input: positive number greater than 10
# output: area for circle
if len(sys.argv) < 2:
    print('no value was provided')
    exit()

try:
    ratio = float(sys.argv[1])
    if ratio>10:
        print('area for circle with ratio = {0}, is {1}'.format(
            ratio,area_of_circle(ratio)))
    else:
        print('this method is valid only values greater than 10')
except ValueError:
    print('value is not a valir number')

