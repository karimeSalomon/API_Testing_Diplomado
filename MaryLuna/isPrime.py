def isPrime(num):
    for val in num:
        prime = 0
    iterator = 2
    if (val == 1 or val == 2):
        print(str(val) + " is prime")
    else:
        while ((val % iterator) != 0):
            prime = 1
            iterator += 1
            if iterator == val: break
        else:
            prime = 0
        if (prime == 0):
            print(str(val) + " is not! prime")
        else:
            print(str(val) + "prime!")


num = map(int, input("Enter a list of numbers separated by comma (Eg: 3,5,4):  ").split(","))

isPrime(num)
