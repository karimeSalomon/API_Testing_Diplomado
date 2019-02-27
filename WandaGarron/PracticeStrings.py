def extract_url(text):
    start = text.find("http://")
    end = text[start:].find(" ")
    print(text[start:start + end])


extract_url("This is the chamilo's http://chamilo.fundacion-jala.org/chamilo/index.php/ URL")


def replace(text, old, new):
    print(text.replace(old, new))

text = "Mississippi"
print(replace(text, "i", "I"))
text = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(text, "om", "am"))
print(replace(text, "o", "a"))