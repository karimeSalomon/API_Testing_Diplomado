song = "I love spom! Spom is my favorite food.Spom, spom, yum!"


def replace(input_string, old_value, new_value):
    words = input_string.split(old_value)
    return new_value.join(words)


print(replace(song, "om", "am"))
print(replace(song, "o", "a"))
