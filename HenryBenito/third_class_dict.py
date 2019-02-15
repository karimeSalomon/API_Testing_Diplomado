song = "ThiS is String with Upper and lower case Letters"


def count(input_string):
    counters = {}
    for char in sorted(list(input_string.replace(' ', '').lower())):
        counters.setdefault(char, 0)
        counters[char] = counters.get(char) + 1
    return counters


print(count(song))
