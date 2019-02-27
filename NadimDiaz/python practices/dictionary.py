def get_data():
    text = input("Input text: ")
    text = text.strip()
    letters = {}
    for char in text:
        if (char.isalpha()):
            letters[char.lower()] = letters.get(char.lower(), 0) + 1
    return dict(sorted(letters.items()))

def print_dict(list):
    print("This is your final list: ", list)

print_dict(get_data())