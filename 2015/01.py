import os
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/01.txt"
)

floor = 0
basement_position = False

with open(input_filepath, encoding = 'utf-8') as f:
  for pointer, cursor in enumerate(list(f.read())):
    if cursor == "(":
      floor += 1
    else:
      floor -= 1

    if floor + 1 == 0 and basement_position == False:
      basement_position = 1 + pointer

print("part 1: %d" % floor)
print("part 2: %d" % basement_position)
