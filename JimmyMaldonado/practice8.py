# Function 1:
# No arguments defined
# Should ask to the user the number of elements in the list
# According the value inserted ask for each value of the
# array and push it in a new array
# Return the array
# 
# Function 2
# Should receive 1 argument (the array returned in method 1)
# should print the array

def function_1():
    """
    Returns an array given its length and values by console
    """

    number_of_elements = int(input("How many elements?: "))
    elements = []
    for i in range(number_of_elements):
        elements.append(int(input("Value for %s?: " % i)))

    return elements


def function_2(array):
    """
    Prints the elements in the array
    """

    for element in array:
        print(element)


my_array = function_1()

function_2(my_array)