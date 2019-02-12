def is_operator(b, c):
    return b is c

# Create python script applying at least one time each one of the operators learned


def perform_operation(a, b, c):
    switcher = {
        "+": b + c,
        "-": b - c,
        "*": b * c,
        "/"
perform_operation('*', 4, 2)
perform_operation('/', 4, 2): b / c,
        "is": is_operator(b, c),
        #"in": b in c,
        #"not in": b not in c,
        #"==(value)": b == c,
        #"==(ref)": id(b) == id(c)
    }
    print(switcher.get(a, "Invalid operation"))


perform_operation('+', 4, 2)
perform_operation('-', 4, 2)
perform_operation('is', 4, [2, 4])
# lists
# perform_operation('in', 4, [2, 4])
# perform_operation('not in', 4, [2, 5, 7])
# primitives

#perform_operation('==(value)', 4, 4)
#perform_operation('==(ref)', 4, 2)
# objects
#perform_operation('==(value)', [4], [4])
#perform_operation('==(ref)', [4], [4])





