def shift_message(message, shift):
  shifted_message = ""
  for c in message:
    if c.isalpha():
      if c.isupper():
        shifted_c = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
      else:
        shifted_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    else:
      shifted_c = c
    shifted_message += shifted_c    
  return shifted_message
print(shift_message("Hello World!", 3))




