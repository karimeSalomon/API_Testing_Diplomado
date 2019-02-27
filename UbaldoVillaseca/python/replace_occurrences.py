def replace(s, old, new):
    return s.replace(old, new)
    
text = "Mississippi"
print(replace(text, "i", "I"))
text = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(text, "om", "am"))
print(replace(text, "o", "a"))
