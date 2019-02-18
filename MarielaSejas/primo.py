min = 10
max = 100

primes = [num for num in range(min,max) if 0 not in [num%i for i in range(2,int(num/2)+1)]]

print (primes)