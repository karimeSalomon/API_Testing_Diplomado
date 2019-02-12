def test1(operator, number1, number2):

    if (operator == "+"):
        print('La operacion es una suma:')
        resultado = number1 * number2
    else:
         print('La operacion no es una Suma XXXXXXX')
         if(operator == "*"):
             print('La operacion es una multiplicacion:')
             resultado = number2 * number1
         else:
            print('La operacion no es una multiplicacion XXXXXX')

            if(operator == '/'):
                resultado=number1 / number2
            else:
                print('La operacion no es una division')
                if (operator == '-'):
                    resultado = number1-number2
                else:
                    print('La operacion no es una resta')

    print (resultado)

test1('*',5,2)