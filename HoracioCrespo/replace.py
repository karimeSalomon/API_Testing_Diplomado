song =  "I love spom! Spom is my favorite food.Spom, spom, yum!"

def replace(s, old, new):
  result_array = []
  words = s.split()
  for word in words:
    find_index = word.find(old)
    if find_index != -1:
      result_array.append(word[0:find_index] + new + word[find_index + len(old):])
    else:
      result_array.append(word)
  
  return " ".join(result_array)


res = replace(song, "om", "am")
print(res)
