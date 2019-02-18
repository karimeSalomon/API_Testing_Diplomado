def sum_char(c, d):
    return d[c] + 1 if d.get(c) else 1


def read_characters(text):
    my_dict = {}
    for char in ''.join(sorted(text.lower())).strip():
        my_dict[char] = sum_char(char, my_dict)

    return my_dict


print(read_characters('ThiS is String with Upper and lower case Letters'))
