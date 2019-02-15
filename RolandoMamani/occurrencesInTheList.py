def occurrenceDictionary(message):
    dictionary = {}

    for char in message:
        dictionary [char] = message.count(char)
        print(char)
        print(message.count(char))

    print(message)

occurrenceDictionary("Holaaa")