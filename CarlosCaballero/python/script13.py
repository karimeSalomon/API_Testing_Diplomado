# practice #11

# create 1 module to calculate age in minutes, hours and days
#
# create 1 module to print 4 different messages:
#   you are a child, when the age is lower than 12
#   your are teenager, when the age is between 13 and 17
#   you are young, when the age is between 18 and 29
#   you are adult, when the age is greater than 30
#
# create a script importing both modules and performing de action:
#   ask to the user the amount of users
#   for all users define the name and the age for each one,
#   save this data as a dictionary 
#
#   after all users are defined, need to:
#       print the age in minutes, hours and days
#       the expected message according the age define

from module01.age import *
from module02.message import *

print('Ingrese la cantidad de usuarios:')
quantity = input()
users = {}

if str.isdigit(quantity):
    count = int(quantity)

    for i in range(count):
        print('=> Ingrese el nombre del usuario #',i+1)

        name = input()
        age = ''

        while not str.isdigit(age):
            print('=> Ingrese la edad de',name)
            age = input()

        users[i] = {
            'name': name,
            'age': int(age)
        }
else:
    print('Numero invalido')
    exit()

for index,user in users.items():
    print('Nombre:',user['name'])
    print('Edad en años:',user['age'])
    print('Edad en dias:',age_days(user['age']))
    print('Edad en horas:',age_hours(user['age']))
    print('Edad en minutos:',age_minutes(user['age']))
    age_message(user['age'])
    print()

