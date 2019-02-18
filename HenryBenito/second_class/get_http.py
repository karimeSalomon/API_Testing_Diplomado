text = "asdasdasdas http://bbc.asddasdas dasdasdasdasdasdasdasdasdasdas0"

http_index = text.index("http://")
end_index = text.index(" ", http_index)

print(text[http_index:end_index])
