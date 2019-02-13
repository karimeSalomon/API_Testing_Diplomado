numero = int(input("Ingrese el numero Porfavor :"))

primos = []
compuestos = []

if numero > 0:
    if numero != 1:
       divisores = []
       for i in range(1,numero+1):
           if numero % i == 0: divisores.append(i)
       if len(divisores) == 2 : print("El numero ingresado es un NUMERO PRIMO")
       else: print("El numero ingresado es un numero compuesto o no es PRIMO")
       print("Sus divisores son: ",divisores)
    else:
        print("El numero 1 no es un numero Primo ni compuesto")
else:
    print("Favor de ingresar un Numero positivo")