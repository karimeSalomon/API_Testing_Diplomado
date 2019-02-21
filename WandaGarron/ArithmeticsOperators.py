firstValue = 5;
secondValue = 10;

print(firstValue + secondValue);
print(firstValue - secondValue);
print(firstValue * secondValue);
print(secondValue/firstValue);
print(secondValue%firstValue);
print(secondValue**firstValue);
print(secondValue//firstValue);

valueToFind = 15
valueOutOfList = 50
list = {1,2,3,10,15,20,25,30,35}

if(valueToFind in list):
    print("The element " + str(valueToFind) + " exist in the list")
else:
    print("Not found element " + str(valueToFind))
if(valueOutOfList in list):
    print("The element " + str(valueOutOfList) + " exist in the list")
else:
    print("The element not found " + str(valueOutOfList))

value_1 = 20
value_2 = 20

if(value_1 is value_1):
    print("Value_1 and Value_2 have same identity")
else:
    print("Value_1 and Value_2 don't have same identity")