import math
import os
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/02.txt"
)

def part1(widths):
    l, w, h = widths

    areas = [
      l * w,
      l * h,
      w * h
    ]

    areas.sort()
    smallest_area = areas[0]
    surface_area = sum(
      [area * 2 for area in areas]
    )
    return smallest_area + surface_area

def part2(widths):
    widths.sort() # smallest widths first
    return sum(
      [v * 2 for v in widths[:2]]
    ) + math.prod(widths)

with open(input_filepath, encoding = 'utf-8') as f:
  instructions = [[int(v) for v in line.strip().split("x")] for line in f]

  needed_papers = [part1(instruction) for instruction in instructions]
  needed_ribbons = [part2(instruction) for instruction in instructions]

  print("part 1: %d" % sum(needed_papers))
  print("part 2: %d" % sum(needed_ribbons))



