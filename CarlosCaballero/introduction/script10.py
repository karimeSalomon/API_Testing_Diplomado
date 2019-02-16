# practice #8

# write a function replace(s,old,new) that replaces all occurences of old with
# new in a string s

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

def replace(string,old,new):
    replaced = ''
    compare = False
    j = 0
    cache = ''

    for i,val in enumerate(string):
        if not compare:
            if val == old[0]:
                compare = True
                j = 1
                cache = old[0]
            else:
                replaced += val
        else:
            if j < len(old):
                if val==old[j]:
                    cache += old[j]
                    j += 1
                else:
                    compare = False
                    replaced += cache
            else:
                compare = False
                replaced += new
        
        if len(old) == j:
            compare = False
            replaced += new
            j = 0

    return replaced

print(replace(example,'o','i'))

