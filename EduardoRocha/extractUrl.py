import re

myString = "This is my tweet check it out http://example.com/blah"

print(re.search("(?P<url>https?://[^\s]+)", myString).group("url"))git