def replace(string, old, new):
    stringAsList = list(string)
    for i in range(len(string)):
        if stringAsList[i] == old:
            stringAsList[i] = new

    return stringAsList


print(replace("Mississippi", "i", "I"))
