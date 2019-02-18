def function_1():
    result = []
    size = int(input("Please enter the size of the list: "))
    for x in range(size):
        result.append(input("Enter a value: "))
    return result


def function_2(content):
    print(content)


function_2(function_1())
