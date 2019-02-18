def stage_of_life(age):
    if age < 12:
        return "You are a child because your age is lower than 12"
    elif  age >= 13 and age <= 17:
        return "You are a teenager, because you age is between 13 and 17"
    elif age >= 18 and age <=29:
        return "You are young, because your age is between 18 and 29"
    elif age > 29:
        print("You are adult, because your age is greater than 30")
        return "You are adult, because your age is greater than 30"

stage_of_life(12)


