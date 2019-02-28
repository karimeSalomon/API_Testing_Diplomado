from CristelhMiranda.python.homework_modules.calculator_module import calculator_helper
from CristelhMiranda.python.homework_modules.printer_module import message_printer


# Homework:
# Ask to the user the amount of users
# For all users define the name and the age for each one, save this data as a dictionary
# After all users are defined, need to :
# print the age in minutes, hours and days
# The expected message according the age define


def build_dictionary():
    cant_inputs = int(input("Enter amount of users: "))
    list_inputs = {}

    for i in range(cant_inputs):
        name = input("Enter name #{}: ".format(i + 1))
        age = input("Enter age #{}: ".format(i + 1))

        list_inputs[name] = age
    return list_inputs


def print_dictionary_values(dict):
    for key in dict:
        print("-----------------------------------------")
        print("User Name: {}".format(key))
        print("Age in mins: {}".format(calculator_helper.calculate_age_mins(dict[key])))
        print("Age in hrs: {}".format(calculator_helper.calculate_age_hours(dict[key])))
        print("Age in days: {}".format(calculator_helper.calculate_age_days(dict[key])))
        message_printer.print_message_evaluating_age(int(dict[key]))
        print("-----------------------------------------")

# Create dictionary
dict = build_dictionary()

# Print dictionary age in mins, hrs and days with its corresponding message
print_dictionary_values(dict)

