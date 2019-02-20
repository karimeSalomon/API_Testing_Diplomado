"""
Practice 11:
      Function 1:
            - No arguments defined
            - Should ask to the user the number of elements in the list
            - According the value inserted ask for each value of the array and push it in a new array
            - Return the array

      Function 2
            - Should receive 1 argument (the array returned in method 1)
            - should print the array
"""

def function1():
    number_of_elements = int(input("Enter the number of elements that list will contain:  "))
    elements = []
    for i in range(number_of_elements):
        elements.append(input("Enter the element:  "))
    return elements

def function2(elements):
    print(elements)


function2(function1())
