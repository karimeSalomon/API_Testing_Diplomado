def print_lyrics():
    "this is the lie reserved fro documentation"
    print ("hola mundo")
    print ("hola mundo 2")


print_lyrics();


def perform_operation():
    "this is the lie reserved fro documentation"
    operator = ["+", "-", "*"]
    for op in operator:
        a = 10
        b = 5
        print(op + " of %s and %s" % (a, b))
        if (op == "+"):
            res = a + b
            if (op == "-"):
                res = a - b
            else:
                res = a * b

        print (res)


perform_operation()
