numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for val in numbers:
    if val%2:
        print("The number is odd", val)
    else:
        print ("The number is even", val)




def get_url(text):
    a = text.find("http://")
    if a != -1:
        return text[a: len(text)].split(' ')[0]
    else:
        return("The is any URL on the text")

print (get_url('ddd  http://fffff fff ffff kk'))







