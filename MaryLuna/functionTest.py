def perform_operation():
    operator = ["+", "-", "*", "/"]
    for op in operator:
        a = 10
        b = 5
        print(op + " of %s and %s" % (a, b))
        if (op == "+"):
            res = a + b
        if (op == "-"):
            res = a - b
        if (op == "*"):
            res = a * b
        if (op == "/"):
            res = a / b

        print(res)

perform_operation();

def perform_operation_2(num_1, num_2, operator):
    print(eval(f'{num_1}{operator}{num_2}'))
perform_operation_2(100, 20, '%')
perform_operation_2(100, 20, '//')
perform_operation_2(10, 2, '+')

