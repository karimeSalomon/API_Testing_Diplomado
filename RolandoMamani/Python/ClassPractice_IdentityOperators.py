"""
Practice 3:   Verify the identity of a variable in the memory.
"""

value_1 = input("Enter the firs number to be compared by identity against a second number:   ")
value_2 = input("Now enter the second number to be compared against previous number:   ")
if (value_1 is value_2):
    print("Line 1 - 'a' and 'b' have same identity")
else:
    print("Line 1 - 'a' and 'b' do not have same identity")

if(id(value_1)==id(value_2)):
    print("Line 1 - 'a' and 'b' have same identity")
else:
    print("Line 1 - 'a' and 'b' do not have same identity")
print("Identity of first number is:  " + str(id(value_1)))
print("Identity of first number is:  " + str(id(value_2)))
