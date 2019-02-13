def get_url(string):
    """ Gets the first occurrence of a url of given text
    :param string: text to look into
    :return: string
    """
    url_start_pos = str.find(string, "http://")
    if url_start_pos > -1:
        new_string = string[url_start_pos: len(string)]
        url_end_pos = str.find(new_string, " ")
        return new_string[0: url_end_pos]
    else:
        return "No url found"


# print results
print(get_url("This is the page http://google.com test it"))
print(get_url("This is the page ht://google.com test it"))
