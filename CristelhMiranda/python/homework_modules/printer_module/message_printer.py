def print_message_evaluating_age(age):
    """ Returns a message according to the specifications below:
            You are a child, when the age is lower than 12
            Your are teenager, when the age is between 13 and 17
            You are young, when the age is between 18 and 29
            You are adult, when the age is greater than 30
    :param age: int
    :return: void
    """
    if age < 12:
        print("You are a child, when the age is lower than 12")
    elif all([age >= 13, age <= 17]):
        print("Your are teenager, when the age is between 13 and 17")
    elif all([age >= 18, age <= 29]):
        print("You are young, when the age is between 18 and 29")
    elif age > 30:
        print("You are adult, when the age is greater than 30")
    else:
        print("....")
