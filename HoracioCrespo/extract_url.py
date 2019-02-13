def extract_url(text):
    index = text.find('http://')
    if index != -1:
        return text[index:len(text)]


text = "the page is http://google.com"
print(extract_url(text))
