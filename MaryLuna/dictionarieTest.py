texto = "fadsaasdasdasdasdafdfdsfdsf"

d = {}

for letra in texto:
    if d.has_key(letra):
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1

    print(d.keys())
    print(d.values())
