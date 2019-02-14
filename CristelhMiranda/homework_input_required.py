def build_array_based_on_inputs():
    """ Returns an array based on given inputs by the user"""
    cant_inputs = int(input("Enter cant of entries: "))
    list_inputs = []

    for i in range(cant_inputs):
        list_inputs.append(input("Enter value #{}: ".format(i+1)))
    return list_inputs


def print_array(array):
    print(array)


# call functions
array = build_array_based_on_inputs()
print_array(array)
