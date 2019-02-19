def get_url(text):
    """ Suppose any line of text can contain at most one url that starts with “http://” and ends at the next space
    in the line. Write a fragment of code to extract and print the full url if it is present. """
    index = text.find('http://')
    if index != -1:
        return text[index: len(text)].split()[0]


print(get_url('test the web http://mywebpage.corm?test=null       is here now available'))
