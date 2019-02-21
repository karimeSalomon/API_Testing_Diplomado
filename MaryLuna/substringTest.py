
def extract_onlyUrl(text):
    ini = text.find("http://")
    end = text[ini:].find(" ")
    return text[ini:ini + end]

def printRes():
    text = "lsdfi sdñflsd shjsdfsdf http://www.google.com "
    print(extract_onlyUrl(text))

printRes()