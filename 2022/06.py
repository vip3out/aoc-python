import os
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/06.txt"
)

def part_fn(streambuffer: str, marker_len: int):
  marker_groups = [
    list(
      set(
        streambuffer[i:i+marker_len]
      )
    ) for i in range(len(streambuffer) -marker_len)
  ]
  counter = 0
  for marker in marker_groups:
    counter += 1
    if len(marker) == marker_len:
      return counter + marker_len - 1

    continue

with open(input_filepath, encoding = 'utf-8') as f:
  streambuffer = f.read()

  print(f"part 1: {part_fn(streambuffer, 4)}")
  print(f"part 14: {part_fn(streambuffer, 14)}")