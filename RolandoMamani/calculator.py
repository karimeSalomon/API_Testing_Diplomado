def my_calculator(operator, number1, number2):
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