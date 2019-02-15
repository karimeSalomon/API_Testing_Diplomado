def substringURL(sentense):
    index_start = sentense.find("http://")

    if(index_start == -1):
        print("The sentence does not contain any http:// URL")
    else:
        index_end = (sentense[index_start:]).find(" ")
        if(index_end == -1):
            url = (sentense[index_start:])
        else:
            url = (sentense[index_start:])[:((sentense[index_start:]).find(" "))]

        print("The URL into the string is:   " + url)

substringURL(input("Enter the string to verify if it contains a url\n"))