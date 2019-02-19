"""
Practice 9:
      - Suppose any line of text can contain at most one url that starts with “http://” and ends at the next space in
        the line. Write a fragment of code to extract and print the full url if it is present.
"""

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

        print("The URL into entered string is:   " + url)

substringURL(input("Enter the string to verify if it contains a url\n"))