# Create 1 module to Calculate age in minutes, hours and days

def calculate_age_in_days(age):
    age_in_days = age * 365
    return age_in_days

def calculate_age_in_hours(age):
    age_in_hours = calculate_age_in_days(age) * 24
    return age_in_hours

def calculate_age_in_minutes(age):
    age_in_minutes = calculate_age_in_hours(age) * 60
    return age_in_minutes

