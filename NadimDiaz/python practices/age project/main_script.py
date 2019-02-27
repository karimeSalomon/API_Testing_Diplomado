import age_calculator
import message_printer


def get_data():
    size_array = int(input("How many elements will have your list?: "))
    coso = {}
    for i in range(0, size_array):
        name = input("Name: ")
        age = int(input("Age: "))
        coso[name] = age
        message_printer.print_message(age)
        age_calculator.calculate_age_withFormat(age)

def print_list(list):
    print("This is your final list: ", list)

print_list(get_data())