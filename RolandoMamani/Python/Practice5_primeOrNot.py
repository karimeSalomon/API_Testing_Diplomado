"""
Practice 5:  According a list of values between a Min and Max range, identify if the number is prime or not.
"""

def isPrimeNumberOrNot(numbers):
    #this funtion verify if a number is prime or not
    for val in numbers:
        prime = 0
        iterator = 2
        if(val == 1 or val == 2):
            print(str(val) + " is prime")
        else:
            while((val%iterator) != 0):
                prime = 1
                iterator +=1
                if iterator == val: break
            else:
                prime = 0
            if(prime == 0):
                print(str(val) + " is not prime")
            else: print(str(val) + " is prime")

numbers = map(int, input("Enter a list of numbers separated by comma (Eg: 3,5,4):  ").split(","))

isPrimeNumberOrNot(numbers)