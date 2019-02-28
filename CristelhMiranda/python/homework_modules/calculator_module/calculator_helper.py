def calculate_age_mins(age):
    return calculate_age_hours(int(age)) * 60


def calculate_age_hours(age):
    return calculate_age_days(int(age)) * 24


def calculate_age_days(age):
    return int(age) * 365
