def isPrime(numMin, numMax):


    limit = numMax +1
    while(numMax < limit):
            if numMin < 1:
                # print (numMin + "no es primo")
                print ("%s no es primo" % numMin)
            elif numMin == 2:
                print (str(numMin) + "es primo")
            else:
                    if numMin % 2 == 0:
                        print ("%s no es primo" % numMin)
                    else:
                        print (str(numMin) + "es primo")
    numMin+=1


isPrime(1, 10)

