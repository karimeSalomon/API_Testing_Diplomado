import math
radio = int(input("Ingrese el radio : "))
def area_of_circle(radio):
    pi = 3.14163
    if radio >= 10 :
        area = math.pow(radio,2)*pi
        print("La area es ",area)
    else:
        print("El radio ingresado es menor que Dies")

area_of_circle(radio)