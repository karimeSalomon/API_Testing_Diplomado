def identify_occurrences(string):
    result = {}
    for char in string:
        char = char.lower()
        # Common if/else statement
        # if char in result:
        #     result[char] = result[char] + 1
        # else:
        #     result[char] = 1

        # ternary operator --> [on_true] if [expression] else [on_false]
        result[char] = (result[char] + 1) if (char in result) else 1
    return result


text = "ThiS is String with Upper and lower case Letters"
print(identify_occurrences(text))
