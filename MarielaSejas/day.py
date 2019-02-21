
def days_in_month(m):

   if (m >= 3 and m<=12 or m==11):
     if(m<=7):
        if(m%2==0):
            print ("el mes " + str(m) + " El mes tiene 30 dias")
        else:
            print ("El mes " + str(m) + " Tiene 31 dias")
     else:
        if(m%2==0):
            print ("El mes " + str(m) + " Tiene 31 dias")
        else:
            print ("El mes " + str(m) + " Tiene 30 dias")
   else:
       if (m==2):
            print ("El mes " + str(m) + " Tiene 28 dias")
       if (m == 1):
            print ("El mes " + str(m) + " Tiene 31 dias")

days_in_month(11)