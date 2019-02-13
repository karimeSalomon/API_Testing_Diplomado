def my_calculator(operator, number1, number2):
    "This function is a calculator for main operator, +, -, * and /"
    if (operator == "*"):
        print("The multimplication of " + str (number1) + "*" + str(number2) + " is " + str(number1 * number2))
    else:
        if(operator == "/"):
            print("The division of " + str(number1) + "/" + str(number2) + " is " + str(number1 / number2))
        else:
            if(operator == "-"):
                print("The subtraction of " + str(number1) + "-" + str(number2) + " is " + str(number1-number2))
            else:
                if(operator == "+"):
                    print("The addition of " + str(number1) + "+" + str(number2) + " is " + str(number1 + number2))
                else:
                    if(operator == "%"):
                        print("The module of " + str(number1) + "%" + str(number2) + " is " + str(number1 % number2))
                    else:
                        if(operator == "//"):
                            print("The floor division of " + str(number1) + "/" + str(number2) + " is " + str(number1 // number2))
                        else:
                            if (operator == "**"):
                                print("The exponent of " + str(number1) + " to " + str(number2) + " is " + str(number1 ** number2))
                            else:
                                print("Sorry, operator not supported by this basic calculator...!!")


my_calculator("//",5,3)