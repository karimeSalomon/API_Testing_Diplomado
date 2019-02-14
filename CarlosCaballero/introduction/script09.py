# practice #7

# suppose any line of text can contain at most one url that starts with
# "http://" and ends at the next space in the line. Write a fragment of code to
# extract and print the full url if it is present

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

def getBlocks(text,prefix,suffix):
    results = []
    index = 0

    while True:
        begin = text.find(prefix,index)

        if(begin==-1):
            return results
        else:
            end = text.find(suffix,begin)
            results.append(text[begin:end].strip())
            index = end

print(getBlocks(example,'http://',' '))

