"""
Practice 12:
       Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order
       which occur in the string together with the number of times each letter occurs.
       Case should be ignored. A sample output of the program when the user enters the data
"""

def buildDictionary(string):

    string = ''.join(sorted(string.casefold()))
    print(string)
    dictionary = {}
    print(dictionary)

    for i in string:
        if(i not in  dictionary):
            dictionary[i] = string.count(i)
            string = string.replace(i, "")

    print(dictionary)

buildDictionary(input("Enter the string in order to generate the diccionary from a string"))

