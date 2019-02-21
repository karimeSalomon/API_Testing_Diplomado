def run_operation(operator, number1, number2):
    operation = number1+operator+number2
    result = eval(operation)
    condition = "The values of the condition were {0} {1} {2}".format(number1, operator, number2)
    print(condition)
    print(str(result))


number1 = '5'
number2 = '6'

run_operation('-', number1, number2)
run_operation('+', number1, number2)
run_operation('*', number1, number2)
run_operation('/', number1, number2)
run_operation('%', number1, number2)
run_operation('==', number1, number2)
run_operation('!=', number1, number2)
run_operation('>', number1, number2)
run_operation('<', number1, number2)
run_operation('>=', number1, number2)
run_operation('<=',number1 , number2)