# Suppose any line of text can contain at most one url
# that starts with "http://" and ends at the next space in
# the line. Write a fragment of code to extract and print
# the full url if it is present.

def get_url(text):
    """
    Prints the embed URL in a given text 
    :param text:
    :return:
    """

    startIndex = text.find("http://")
    substring = text[startIndex:len(text)]
    endIndex = substring.find(" ")
    print(substring[0:endIndex])


random_text_1 = " hi hi hi http://google.com hi hi"
get_url(random_text_1)

random_text_2 = " Visit http://www.umss.com for more information"
get_url(random_text_2)