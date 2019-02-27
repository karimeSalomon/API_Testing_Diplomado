# practice #12

# Create 1 module to Calculate the area of a circle :
# radius * 2 * pi
# create 1 module to calculate the perimeter of a circle:
# radius * radius * pi
# create a script to ask to the user of the radio and print both results.

from module03.area import area
from module04.perimeter import perimeter

print('Ingrese el radio de la circunferencia')
ratio = input()

if str.isdigit(ratio):
    ratio = int(ratio)
    print('Area de la circunferencia:',area(ratio))
    print('Perimetro de la circunferencia:',perimeter(ratio))
else:
    print('Numero invalido')

