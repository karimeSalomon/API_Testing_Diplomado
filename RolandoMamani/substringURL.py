def substringURL(sentense):
    index_start = sentense.find("http://")
    print(index_start)
    if(index_start == -1):
        print("The sentence does not contain any http:// URL")
    else:
        for x in sentense:
            print(x)
            if(x==" "):
                index_end = sentense.find(" ")
                print("Encontre el espacio")



substringURL("Hola mundo http://jj jj")