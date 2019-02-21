import calculate_age
import messages_for_age

def amount_of_users():
    users = {}
    number_of_users = int(input("How many user?"))
    print("text", number_of_users)

    for i in range(number_of_users):
        user_name = input("Insert name:")
        user_age = int(input("Inser age:"))
        users[user_name] = user_age

    for i in users:
       print("Information for user:", i)
       calculate_age.calculate_age_in_days(users[i])
       calculate_age.calculate_age_in_hours(users[i])
       calculate_age.calculate_age_in_minutes(users[i])
       #print("User age", i)

amount_of_users()