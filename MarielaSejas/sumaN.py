def sum_to(n):

    if n <= 35:
        sum = 0
        for i in range(1, n+1):
            sum = sum + int(i)
        print(sum)

    else:
     print("The suma is not possible because the n is greater than 35")


sum_to(10)