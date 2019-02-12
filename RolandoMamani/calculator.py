def my_calculator(operator, number1, number2):
    "This function is a calculator for main operator, +, -, * and /"
    if (operator == "*"):
        print(number1 * number2)
    else:
        if(operator == "/"):
            print(number2/number2)
        else:
            if(operator == "-"):
                print(number1-number2)
            else:
                if(operator == "+"):
                    print(number1+number2)
                else:
                    print("Sorry, operator not supported by this basic calculator...!!")

my_calculator("//",5,5)