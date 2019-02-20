# Write a program that reads a string and returns a table of the letters of the
# alphabet in alphabetical order which occur in the string together with the
# number of times each letter occurs.
# 
# Case should be ignored. A sample output of the program when the user
# enters the data
# "ThiS is String with Upper and lower case Letters", would look this this => 
# a 2
# c 1
# d 1
# e 5
# g 1
# h 2
# i 4
# l 2
# n 2
# o 1
# p 2
# r 4
# s 5
# t 5
# u 1
# w 2

def count_letters(text):
    """
    Count the number of repeated letters in a given text and prints the results in console
    """

    counter = {}
    text = text.replace(' ', '').lower()
    
    for letter in sorted(text):

        if letter not in counter:
            counter[letter] = 0            
        
        counter[letter] += 1

    print(counter) 


count_letters("hello world")

count_letters("ThiS is String with Upper and lower case Letters")