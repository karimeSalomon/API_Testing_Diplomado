def execute_operation(number_1, number_2, operator_1):
    switcher = {
        '+': (number_1 + number_2),
        '-': (number_1 - number_2),
        '*': (number_1 * number_2),
        '/': (number_1 / number_2)
    }
    return switcher.get(operator_1, 'nothing')

addition_result = execute_operation(1, 2, '+')
print(addition_result)