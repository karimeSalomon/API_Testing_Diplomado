def get_input():
    number_of_elements = int(input("Type the number of elements in the list: "))
    list = []
    for i in range(0, number_of_elements):
        list.append(int(input("Type the element to append: ")))
    return list

def print_array(array):
    print("Array is", array)

print_array(get_input())