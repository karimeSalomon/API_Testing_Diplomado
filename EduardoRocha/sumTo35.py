
def sum_numbers(x):
    result = []
    for y in range(0,x):
        result.append(y)
    b = sum(result)
    if b >35:
        print('the sum in more greather than 35')
    else:
        print(int(b))





sum_numbers(20)
