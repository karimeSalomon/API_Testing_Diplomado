def count_letters(text):
    coincidences = {}
    for char in text.replace(" ", ""):
        coincidences[char.lower()] = coincidences.get(char.lower(), 0) + 1
    return dict(sorted(coincidences.items()))

print(count_letters("ThiS is String with Upper and lower case Letters"))