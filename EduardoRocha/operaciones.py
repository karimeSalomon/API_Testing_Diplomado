primerNumero  = 1
segundoNumero = 2
resultadoSuma = primerNumero+segundoNumero
resultadoResta =segundoNumero-primerNumero
resultadoMultiplicacion = primerNumero*segundoNumero
resultadoDivision = segundoNumero/primerNumero
print("Suma=",resultadoSuma)
print("Resta=",resultadoResta)
print("Multiplicacion=",resultadoMultiplicacion)
print("Division=", resultadoDivision)

a = 6
b = 55
list = [1, 2, 3, 4, 5];


if ( a in list ):
    print("a exists list")
else:
   print("a does not exist list")

if ( b not in list ):
    print("b does not exist list")
else:
    print("b exists list")

value_1 = 200
value_2 = 2010

if ( value_1 is value_2 ):
   print("Line 1 - a and b have same identity")
else:
   print('Line 1 - a and b do not have same identity')

if ( id(value_1) == id(value_2) ):
   print("Line 2 - a and b have same identity")
else:
   print("Line 2 - a and b do not have same identity")
   print( "id for value 1 =",id(value_1))
