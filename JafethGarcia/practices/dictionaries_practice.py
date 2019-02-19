def sum_char(c, d):
    return d[c] + 1 if d.get(c) else 1


def read_characters(text):
    """ Write a program that reads a string and returns a table of the letters
    of the alphabet in alphabetical order which occur in the string together
    with the number of times each letter occurs.
    Case should be ignored. A sample output of the program when the user
    enters the data

    “ThiS is String with Upper and lower case Letters”, would look this this =>
        a 2
        c 1
        d 1
        e 5
        g 1
        h 2
        i 4
        l 2
        n 2
        o 1
        p 2
        r 4
        s 5
        t 5
        u 1
        w 2
    """
    my_dict = {}
    for char in ''.join(sorted(text.lower())).strip():
        my_dict[char] = sum_char(char, my_dict)

    return my_dict


print(read_characters('ThiS is String with Upper and lower case Letters'))
