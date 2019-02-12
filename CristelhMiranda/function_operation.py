# Create python script applying at least one time each one of the operators learned
def perform_operation(a, b, c):
    try:
        res = eval("b " + a + " c")
        return f"{b} {a} {c} {'='} {res}"
    except TypeError as e:
        print("Invalid operation for operator: " + a + str(e))
    except SyntaxError as e:
        print(str(e))


print(perform_operation('+', 4, 2))
print(perform_operation('-', 4, 2))
print(perform_operation('*', 4, 2))
print(perform_operation('/', 4, 2))
print(perform_operation("is", 4, 4))
print(perform_operation("is not", 4, 4))
# lists
print(perform_operation('in', 4, [2, 4]))
print(perform_operation('not in', 4, [2, 4]))
# compare int values
print(perform_operation('==', 4, 4))
print(perform_operation('==', 4, 2))
# objects
print(perform_operation('==', [4], [4]))
print(perform_operation('==', [4], [2]))
# Exceptions
print(perform_operation('+', 4, [2]))
print(perform_operation('wrongSyntax', 4, [2]))
