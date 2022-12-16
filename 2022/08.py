import os
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/08.txt"
)

tree_map = []

with open(input_filepath, encoding = 'utf-8') as f:
  for line in f:
    tree_map.append(list(line.strip()))

print(tree_map)
