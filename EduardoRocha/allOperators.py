def operacionesBasicas(firstNumber,operator, secondNumber):
    if (operator == "+"):
        resultado = (firstNumber +secondNumber)
    elif(operator == "-"):
        resultado =(firstNumber-secondNumber)
    elif(operator=="*"):
        resultado= firstNumber*secondNumber
    elif(operator=="/"):
        resultado=firstNumber/secondNumber

    if (firstNumber != secondNumber):
        print ('the numbers are distinct')
        if(firstNumber>secondNumber):
            print(firstNumber, 'is more greater than',secondNumber)
        elif(firstNumber <= secondNumber):
                print(firstNumber,'is less o equals to', secondNumber)



    print (resultado)

while True:
    a = input('[+] Enter a number')
    b = input('[+] Enter a second number')
    op = input('[+] Enter an operation')

    operacionesBasicas(int(a), op, int(b))


