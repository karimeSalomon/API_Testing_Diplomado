def extract_url(text):
    start = text.find("http://")
    end = text[start:].find(" ")
    return text[start:start + end]

def main():
    text = "I'm drakula and this is my facebook: http://www.facebook.com/drakula ulaualua"
    print("Extracting:", extract_url(text))
    
main()