from collections import OrderedDict


text = "ThiS is String with Upper and lower case Letters"

def count_letters(text):
    orderedText = sorted(text.lower().replace(" ", ""))
    letters_dict = OrderedDict()
    for letter in orderedText:
        letters_dict[letter] = letters_dict.get(letter, 0) + 1
    return letters_dict


print(count_letters(text));
