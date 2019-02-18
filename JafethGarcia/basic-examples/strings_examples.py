def get_url(text):
    index = text.find('http://')
    if index != -1:
        return text[index: len(text)].split()[0]


print(get_url('test the web http://mywebpage.corm?test=null       is here now available'))
