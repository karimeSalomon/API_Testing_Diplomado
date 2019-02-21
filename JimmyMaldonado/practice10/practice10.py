# Create 1 module to Calculate age in minutes, hours and days ==> module1.py
#
# Create 1 module to print 4 different messages: ==> module2.py
#   * You are a child, when the age is lower than 12
#   * Your are teenager, when the age is between 13 and 17
#   * You are young, when the age is between 18 and 29
#   * You are adult, when the age is greater than 30
#
# Create a script importing both modules and performing de action: ==> practice10.py
#   * Ask to the user the amount of users
#   * For all users define the name and the age for each one, save this data as a
#   dictionary
#   * After all users are defined, need to :
#       * Print the age in minutes, hours and days
#       * The expected message according the age define

import module1
import module2

def main():
    """
    Prints the users' information given the amount of users, names and ages.
    """
    users = {}
    amount_of_users = int(input("How many users?: "))

    for index in range(amount_of_users):
        name = input("What's your name?: ")
        age = int(input("How old are you?: "))
        users[index] = (name, age)
        print()

    for key in users:
        print("Key:", key, "User:", users[key])
        module1.calculate_age_in_minutes(users[key][1])
        module1.calculate_age_in_hours(users[key][1])
        module1.calculate_age_in_days(users[key][1])
        module2.print_age_message(users[key][1])
        print()
        

main()