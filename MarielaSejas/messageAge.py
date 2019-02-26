def message(edad):

    if edad > 0  and edad <= 12:
        result= print ("You are child")
    if edad >= 13 and edad <=17:
        result = print ("You are teenager")
    if edad >= 18 and edad <= 29:
        result= print("You are young")
    if edad >= 30:
        result = print("You are adult")
    return result