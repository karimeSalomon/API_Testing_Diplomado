# def imprimir():
#     "Esto es una descripcion de Python"
#     print("Pertenesco a la funcion imprimir")
# print("Soy Efrain y estoy aprendiendo a usar funciones")
# imprimir()

def multiplicacion(operador,a,b):
    print("El valor de a es = "+str(a))
    print("El valor de b es = " + str(b))
    print("El operador es: " + operador)
    print("------------------------------")
    if(operador is "*"):
        multi = a*b
        print("La multiplicacion a*b es = "+str(multi))
    if(operador is "+"):
        print("La suma (a+b) es = "+str(a+b))
    if(operador is "-"):
        print("La Resta (a-b) es = "+str(a-b))
    if(operador is "/"):
        print("La division de (a/b) es = "+str(a/b))
    if(operador is "%"):
        print("El modulo es (a%b) = "+str(a%b))
    print("------------------------------")
multiplicacion("*",5,2)