def get_url(text):
    a = text.find("http://")
    if a != -1:
        return text[a: len(text)].split(' ')[0]
    else:
        return("There is any URL on the text")

print (get_url('esta url redirecciona a google http://www.google.com/ fff ffff kk'))