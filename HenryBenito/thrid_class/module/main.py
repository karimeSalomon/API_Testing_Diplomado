from calculate import *
from printer import *

users_number = int(input("How many users you want to create: "))
users = {}

for user in range(users_number):
    name = input("User name: ")
    users[name] = float(input("Age: "))

print(users.items())
for name, age in users.items():
    print("=============================================")
    print("Hey {}!".format(name))
    print("=============================================")
    print("Your age in days is {}".format(in_days(age)))
    print("Your age in hours is {}".format(in_hours(age)))
    print("Your age in mins is {}".format(in_mins(age)))

    if age < 13:
        print_child()
    if 12 < age < 18:
        print_teenager()
    if 17 < age < 31:
        print_young()
    if age > 30:
        print_adult()

    print("=============================================")
