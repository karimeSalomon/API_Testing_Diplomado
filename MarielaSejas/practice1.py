def print_TestMariela(a, b, c):
    "Iniciando el primer ejemplo para poder obtener el resultado de una operacion"

    if (a == "*"):
        resultado = b*c
        print("El resultado de la multiplicion entre  " +str(b) + " = " +str(c) + " es:")


    if (a == "/"):
        resultado = b / c
        print("El resultado de la division entre  " + str(b) + " = " + str(c) + " es:")

    if (a == "-"):
        resultado = b - c
        print("El resultado de la resta entre  " + str(b) + " = " + str(c) + " es:")

    if (a == "+"):
        resultado = b + c
        print("El resultado de la suma entre  " + str(b) + " = " + str(c) + " es:")

    if (a == "%"):
        resultado = b % c
        print("El resultado del modulo entre  " + str(b) + " = " + str(c) + " es:")

    if (a == "**"):
        resultado = b ** c
        print("El resultado del exponente entre  " + str(b) + " = " + str(c) + " es:")

    if (a == "//"):
        resultado = b // c
        print("El resultado del Floor Division entre  " + str(b) + " = " + str(c) + " es:")

    print(resultado)


print_TestMariela("//", 5, 5)