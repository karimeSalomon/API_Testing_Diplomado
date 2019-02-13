numero = int(input("Ingrese el numero porfavor : "))
def suma_to(numero):
    suma = ""
    total = 0
    if numero > 0:
        for a in range(1,numero+1):
            if a>35: break
            suma = suma+"+"+str(a)
            total += a
        print("La suma es : ",suma,"=",total)
    else: print("Ingrese un numero positivo porfavor")
suma_to(numero)