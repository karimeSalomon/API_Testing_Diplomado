"""
Practice 10:
      Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:
            -  replace("Mississippi", "i", "I") == "MIssIssIppI"
            -  song = "I love spom! Spom is my favorite food. Spom, spom, yum!"
               replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam,spam, yum!"
               replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam,spam, yum!"
"""


def replace(s, old, new):
    message_changed = s.split(old)
    message_changed = new.join(message_changed)
    print(message_changed)

message = input("Please, enter the message:  ")
old = input("enter the letter or word to be changed in the message:  ")
new = input("enter the new letter or word that will replace the previous letter/word in the message:  ")

replace(message, old, new)