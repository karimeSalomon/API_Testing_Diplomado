def extract_url(text):
    start = text.find("http://")
    end = text[start:].find(" ")
    return text[start:start + end]

def main():
    text = "There is a URL like http://drive.google.com/drive/folders/1LHtSvHkKr0ix5GoZW0QBOgxrnGcfkHRg in this text"
    print(extract_url(text))
    
main()