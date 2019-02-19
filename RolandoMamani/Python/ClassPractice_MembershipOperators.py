
"""
Practice 2:   Verify if the variable a exist in the listA and if variable b does not exist in the ListB
"""
a = input("Enter a letter between a to z to be searched in list A:   ")
b = input("Enter a letter between a to z to be searched in List B:   ")
listA = ["z", "g", "a", "c", "k"]; listB = ["q", "a", "l", "r", "x"]

if(a in listA):
    print("a exist in the list A")
else:
    print("a is not in the list A")
if(b not in listB):
    print("b does not exist in the list B")
else:
    print("b exist in the list B")