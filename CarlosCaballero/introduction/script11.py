# practive #9

# write the program that reads a string and returns a table of the letters of
# the alphabet in alphabetical order which occur in the string together with the
# number of times each letters occurs.
# - case should be ignored. A sample output of the program when the user enters
# the data

example = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas
    lobortis quam augue, a http://www.google.com.bo tincidunt risus egestas
    vel. Cras libero urna, iaculis nec nisl vitae, sagittis porttitor massa.
    Donec sem tellus, dapibus vitae rhoncus pretium, http://www.yahoo.com
    egestas eu urna. Praesent lectus nisi, ornare vitae tortor ac, rhoncus
    vulputate nulla. Etiam lacinia consequat diam in laoreet. Integer dictum
    est quis neque hendrerit semper. Integer eleifend ullamcorper velit, in
    posuere augue sollicitudin sit amet. Nam id pellentesque turpis.
    """

def counter(text):
    table={}

    for letter in text:
        if letter.isalnum():
            letter = letter.lower()

            if letter in table:
                table[letter] += 1
            else:
                table[letter] = 1
    
    return table

table = counter(example)
for key in sorted(table.keys()):
    print('{0} => {1}'.format(key,table[key]))

