def area_of_circle(r):

    if r > 10:
        pi = 3.1416
        area = (pi * (r ** 2))
        print ("El area del circulo es:")
        print (area)
    else:
        print ("El area no sera mostrada por que el radio es menor o igual a 10")
area_of_circle(11)