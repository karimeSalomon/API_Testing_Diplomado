def perform_operation(operator, num_1, num_2):
    """Performs the given operation"""

    if operator == "*":
        return num_1 * num_2
    if operator == "+":
        return num_1 + num_2
    if operator == "-":
        return num_1 - num_2
    if operator == "/":
        return num_1 / num_2


print(perform_operation("*", 2, 8))

print(perform_operation("+", 2, 8))

print(perform_operation("-", 2, 8))

print(perform_operation("/", 2, 8))