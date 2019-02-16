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

    else:
        print("No se encontro el operador especificado")


function_three_arguments("*",4, 3)
function_three_arguments("-",4, 3)
function_three_arguments("+",4, 3)
function_three_arguments("/",4, 3)
function_three_arguments("%",4, 3)
