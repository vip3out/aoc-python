import os
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/07.txt"
)

def is_command(line):
  return True if line[0] == "$" else False

def is_dir(line):
  return True if line[0:3] == "dir" else False

file_tree = []
current_dir = False

with open(input_filepath, encoding = 'utf-8') as f:
  for line in f:
    line = line.strip()
    instruction = line.split(" ")
    if is_command(line) == True:
      command = instruction[1]
      current_dir = instruction[2] if command == "cd" else current_dir

    if current_dir:
      print(current_dir)

