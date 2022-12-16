from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=6)

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

def part_a():
  return part_fn(puzzle.input_data, 4)
def part_b():
  return part_fn(puzzle.input_data, 14)
