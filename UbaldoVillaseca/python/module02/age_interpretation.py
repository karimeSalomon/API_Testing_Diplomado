def interpret(age):
  if age < 12:
    return "You are a child"
  elif age <= 17:
    return "You are a teenager"
  elif age <= 29:
    return "You are young"
  
  return "You are adult"
  