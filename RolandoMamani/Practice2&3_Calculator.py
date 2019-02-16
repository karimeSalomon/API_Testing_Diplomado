"""
Practice 2:
    Create a function that receive 3 arguments :
        -     2 numbers
        -     1 operations
    According the operation defined the expected result need to be printed. For example :  operator “*” , numbers: “5” “6”, perform_operation(“*”,”5”,”6”) => 30
"""


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


print("You need to add the operation and the two numbers to calculate the result, valid operators are '+', '-', '*', '/', '%', '**', '//'")

operator = input("Please enter the operator:  ")
number1 = input("Please enter the first number:  ")
number2 = input("Please enter the second number:  ")

my_calculator(operator, int(number1), int(number2))