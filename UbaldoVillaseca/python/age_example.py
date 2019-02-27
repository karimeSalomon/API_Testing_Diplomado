from module01.age import *
from module02.age_interpretation import *

number_of_users = int(input("Type the amount of users: "))
users = {}
for i in range(0, number_of_users):
  name = input(f"Type the name of user {i}: ")
  age = int(input("Now his/her age: "))
  users[name] = age
 
for name, age_in_years in users.items():
  age_in_minutes = age_minutes(age_in_years)
  age_in_hours = age_hours(age_in_years)
  age_in_days = age_days(age_in_years)
  interpretation = interpret(age_in_years)
  print(f'Age in minutes/hours/days for user {name} is {age_in_minutes}/{age_in_hours}/{age_in_days}. {interpretation}')
