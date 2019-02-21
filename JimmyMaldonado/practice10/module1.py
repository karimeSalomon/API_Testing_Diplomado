# Create 1 module to Calculate age in minutes, hours and days

def calculate_age_in_minutes(age):
    """
    Calculates the age in minutes
    """

    age_in_minutes = age * 365 * 24 * 60
    print("Age in minutes:", age_in_minutes)


def calculate_age_in_hours(age):
    """
    Calculates the age in hours
    """

    age_in_hours = age * 365 * 24
    print("Age in hours:", age_in_hours)


def calculate_age_in_days(age):
    """
    Calculates the age in days
    """

    age_in_days = age * 365
    print("Age in days:", age_in_days)