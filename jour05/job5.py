def calculate_distance(num_steps, step_height):
  distance = num_steps * step_height / 100
  distance += num_steps * step_height / 100
  distance *= 7
  return round(distance, 2)
