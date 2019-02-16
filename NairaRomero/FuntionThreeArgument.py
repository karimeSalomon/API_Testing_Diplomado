def function_three_arguments( operator, op2, op1):

    if(operator == "+"):
        result= op1+op2
        print("Es una suma =", result )
    elif(operator == "-"):
        result= op1-op2
        print("Es una resta =", result)
    elif(operator == "*"):
        result= op1*op2
        print("Es una multiplicacion =", result)
    elif(operator == "/"):
        result= op1/op2
        print("Es una division =", result)
    elif(operator == "is"):
        result = op1 is op2
        if(result):
            print(" El emento se encuentra en la list?-->", result)
        else:
            print("El elemento no se encuentra en la lista", result)

    else:
        print("No se encontro el operador especificado")


function_three_arguments("*",4, 3)
function_three_arguments("-",4, 3)
function_three_arguments("+",4, 3)
function_three_arguments("/",4, 3)
function_three_arguments("+++",4, 3)
function_three_arguments("is",4, [1,2,5,7,8])