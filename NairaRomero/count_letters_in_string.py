def counts_letter_in_String(string):
    dict = {}
    string = string.casefold()
    for i in range(len(string)):
        aux = string[i]
        count = 0
        for a in range(len(string)):
            aux2 = string[a]
            if aux2 == aux:
                count+=1
        dict[aux] = count

    print("Dictionary", dict)






counts_letter_in_String("hh d f h f Dd ll Hf asdFghj asDsdffG")