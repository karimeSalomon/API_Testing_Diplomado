def countOccurrences(text):
    occurrences = {}
    textInLowerCase = text.lower()
    print(textInLowerCase)
    for letter in textInLowerCase:
        if(letter is ' '): continue
        times = textInLowerCase.count(letter)
        occurrences[letter] = times
    return occurrences


result = countOccurrences('Jajaja')
print(result)

# Suppose any line of text can contain at most one url that starts with “http://”
# and ends at the next space in the line. Write a fragment of code to extract and print the full url if it is present.


def extract_url(text):
    textSplitted = text.split()
    for word in textSplitted:
        if('http' in word ):
            return word


url = extract_url('este es el url:http://test.something.com:4200 de la página')
print(url)

