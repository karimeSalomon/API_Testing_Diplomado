# Ask to the user the amount of users
# For all users define the name and the age for each one, save this data as a dictionary
# After all users are defined, need to :
# print the age in minutes, hours and days
# The expected message according the age define
import Module1 # as age_operations
import Module2 # as age_messages

# For all users define the name and the age for each one, save this data as a dictionary
def init_users():
    n_users = int(input("Enter the amount of users: "))
    users = {}
    for i in range(0, n_users):
        name = (input('{} - Enter the name : '.format(i)))
        age = int(input('{} - Enter the age: '.format(i)))
        users[name] = age
    return users


def show_age_calculations(age):
    age_in_days = Module1.calculate_age_in_days(age)
    print('Age in days: ', age_in_days)

    age_in_hours = Module1.calculate_age_in_hours(age)
    print('Age in hours: ', age_in_hours)

    age_in_minutes = Module1.calculate_age_in_minutes(age)
    print('Age in minutes: ', age_in_minutes)


# print the age in minutes, hours and days. The expected message according the age define
def users_age_stages(users_list):
    for name, age in users_list.items():
        print(name, ' - ', age, ' years old')
        show_age_calculations(age)
        Module2.print_age_stage(age)


users = init_users()
users_age_stages(users)
