def replace(s, old, new):
    return s.replace(old, new)
    
text = "Mississippi"
print("basic case:", replace(text, "i", "I"))
text = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print("first case:", replace(text, "om", "am"))
print("second case:", replace(text, "o", "a"))