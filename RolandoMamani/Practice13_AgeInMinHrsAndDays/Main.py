"""
Practice 13:
    - Create 1 module to Calculate age in minutes, hours and days
    - Create 1 module to print 4 different messages :
            - You are a child, when the age is lower than 12
            - Your are teenager, when the age is between 13 and 17
            - You are young, when the age is between 18 and 29
            - You are adult, when the age is greater than 30
    - Create a script importing both modules and performing de action :
            - Ask to the user the amount of users
            - For all users define the name and the age for each one, save this data as a dictionary
            - After all users are defined, need to :
                    * print the age in minutes, hours and days
                    * The expected message according the age define
"""


import lib.AgeCalculator as AgeCalculator
import lib.AgePrinter as AgePrinter

users = {}

def readUserInformation():
    amount_of_iusers = int(input("Enter the amount of users you want to register:  "))
    for i in range(amount_of_iusers):
        user_name = input("Please, enter the user name:  ")
        user_age = input("Please, enter the age for " + user_name + ":  ")
        users[user_name] = user_age

def printUsersAge():
    print("Users age is as following in days, hours and minutes:")
    print("----------------------------------------------------------------------------------------------------")
    for i in users:
        print(i + " is " + users[i] + " years old. Then " + i + " ", end="")
        AgePrinter.printAge(int(users[i]))
        print("     Age in days:     " + str(AgeCalculator.calculateAgeInDays(int(users[i]))))
        print("     Age in hours:    " + str(AgeCalculator.calculateAgeInHours(int(users[i]))))
        print("     Age in minutes:  " + str(AgeCalculator.calculateAgeInMinutes(int(users[i]))))
        print("----------------------------------------------------------------------------------------------------")

readUserInformation()
printUsersAge()