def isPrimeNumberOrNot(numbers):
    #this funtion verify if a number is prime or not
    for val in numbers:
        primo = 0
        iterator = 2
        while((val%iterator) != 0):
            primo = 1
            iterator +=1
            if iterator == val: break
        else:
            primo = 0
        if(primo == 0):
            print(str(val) + " is not prime")
        else: print(str(val) + " is prime")

isPrimeNumberOrNot([10,5,3])