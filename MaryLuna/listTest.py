def read_numbers():
    number_of_elements = int(input("set numbers: "))
    listNum = []
    for i in range(0, number_of_elements):
        listNum.append(int(input("append: ")))
    return listNum

def print_list(array):
    print("Array is", array)

print_list(read_numbers())
