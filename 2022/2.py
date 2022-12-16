from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=2)

player    = ["X","Y","Z"]
oppenent  = ["A","B","C"]

def part_a():
  score = 0
  wins = [-1, 2]

  for line in puzzle.input_data.splitlines():
    a, b = line.strip().split(" ")
    playerIdx = player.index(b)

    value = oppenent.index(a) - playerIdx
    points = 6 if value in wins else 3 if value == 0 else 0
    score += playerIdx + 1 + points

  return score

def part_b():
  score = 0
  for line in puzzle.input_data.splitlines():
    a, b = line.strip().split(" ")
    playerIdx = player.index(b)

    trans_op = (oppenent.index(a) + 2) % 3
    selected_index = (playerIdx + trans_op) % 3
    points = 6 if playerIdx > 1 else 3 if playerIdx == 1 else 0
    score += selected_index + 1 + points

  return score