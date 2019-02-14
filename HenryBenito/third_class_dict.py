song = "ThiS is String with Upper and lower case Letters"


def count(input_string):
    chars_list = list(input_string.lower()).sort()
    counters = {}
    for char in chars_list:
        counters.setdefault(char, 0)
        counters[char] = counters.get(char) + 1
    return counters


print(count(song))
