def calculate_age_in_days(age):
    age_in_days = age * 365
    print ("Your age in days is", age_in_days)
    return age_in_days


#calculate_age_in_days(25)

def calculate_age_in_hours(age):
    age_in_hours = calculate_age_in_days(age) * 24
    print("Your age in hours is", age_in_hours)
    return age_in_hours

#calculate_age_in_hours(25)

def calculate_age_in_minutes(age):
    age_in_minutes = calculate_age_in_hours(age) * 60
    print("Your age ins minutes is", age_in_minutes)
    return age_in_minutes

calculate_age_in_minutes(25)