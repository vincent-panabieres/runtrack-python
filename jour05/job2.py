def draw_rectangle(width, height):
  print("+" + "-" * width + "+")
  print("|" + " " * width + "|")
for i in range(height - 2):
  print("|" + " " * width + "|")
if height > 1:
  print("|" + " " * width + "|")
print("+" + "-" * width + "+")
draw_rectangle(10, 3)