from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=4)

pairs = [pair.strip().split(",") for pair in puzzle.input_data.splitlines()]

def getLengthsFromPair(pair):
  section_a, section_b = sorted(
    [
      list(range(int(a), int(b)+1)) for a,b in [
        section.split("-") for section in pair
      ]
    ],
    key=len
  )
  return [
    len([found for found in section_a if found in section_b]),
    len(section_a)
  ]

def part_a():
  count = 0
  for pair in pairs:
    lFounds, lSectionA = getLengthsFromPair(pair)
    count += 1 if lFounds == lSectionA else 0

  return count
def part_b():
  count = 0
  for pair in pairs:
    lFounds, _ = getLengthsFromPair(pair)
    count += 1 if lFounds > 0 else 0

  return count

