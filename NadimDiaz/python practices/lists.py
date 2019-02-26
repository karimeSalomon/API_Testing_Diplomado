def get_data():
    size_array = int(input("How many elements will have your list?: "))
    list = []
    for i in range(0, size_array):
        list.append(int(input("Type the element to add to the list: ")))
    return list

def print_list(list):
    print("This is your final list: ", list)

print_list(get_data())