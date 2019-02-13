import operator
import re

def get_operator(operatorInput):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
        "//": operator.floordiv,
        "**": operator.pow
    }
    return operators.get(operatorInput)

def perform_operation(operatorInput, first_value, second_value):
    return get_operator(operatorInput)(first_value, second_value)

def is_valid_operator(operatorInput):
    re_operators= '^(\+|-|\*|\/|%|\/\/|\*\*)$'
    return bool(re.match(re_operators, operatorInput))

def is_valid_number(value):
    try:
        value = float(value)
        return True
    except:
        return False

def start():
    first_value = input("Please enter first value: ")
    second_value = input("Please enter second value: ")
    operatorInput = input("Please enter operator: ")
    
    if not(is_valid_number(first_value)):
        print("wrong value for first parameter")
    if not(is_valid_number(second_value)):
        print("wrong value for second parameter")
    if not(is_valid_operator(operatorInput)):
        print("wrong value for operator")
    else:
        result = perform_operation(operatorInput, float(first_value), float(second_value))
        print("Result= {}".format(result))


start()