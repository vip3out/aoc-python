from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=24)

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

START = [0,1]
MOVES = [
  [0, 1],
  [1, 0],
  [-1, 0],
  [0, -1]
]
MOVE_EXPRESSION = list(">v^<")
MOVE_NAMINGS = "rightwards, downwards, upwards, leftwards".split(", ")

input_data = puzzle.input_data
input_data_lines = input_data.splitlines()
# input_data = """#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#"""
# input_data_lines = input_data.split("\n")
input_data_matrix = [list(row) for row in input_data_lines]

class Point:
  def __init__(self, pos):
    self._x = pos[1]
    self._y = pos[0]

  @property
  def y(self) -> int:
    return self._y

  @property
  def x(self) -> int:
    return self._x

  @y.setter
  def y(self, y):
    self._y = y

  @x.setter
  def x(self, x):
    self._x = x

  def __str__(self) -> str:
    return f"({self.y}, {self.x})"

  def __iter__(self) -> list:
   return iter([self.y, self.x])
class Blizzard:
  def __init__(self, v, pos):
    self.v = v
    self._pos = Point(pos)

  @property
  def pos(self) -> list:
    return list(self._pos)

  @property
  def move(self) -> list:
    return MOVES[MOVE_EXPRESSION.index(self.v)]

  @property
  def direction(self) -> list:
    return MOVE_NAMINGS[MOVE_EXPRESSION.index(self.v)]

  def moving(self, bottomRightCorner):
    x = self._pos.x + self.move[1]
    y = self._pos.y + self.move[0]

    self._pos.x = bottomRightCorner.x - 1 if x == 0 else x if x < bottomRightCorner.x else 1
    self._pos.y = bottomRightCorner.y - 1 if y == 0 else y if y < bottomRightCorner.y else 1

  def __str__(self) -> str:
    return f"Blizzard at ({self._pos}) moving {self.direction}"

def onTarget(pos, target):
  return True if pos.x == target.x and pos.y == target.y else False

def onBounds(pos, bottomRightCorner):
  if pos.x == 0 or pos.y == 0:
    return True

  if pos.x == bottomRightCorner.x or pos.y == bottomRightCorner.y:
    return True

  return False

def onAnyBlizzard(pos, blizzards):
  return list(pos) in [blizzard.pos for blizzard in blizzards]

def moving(pos, move):
  return Point(
    [pos.y + move[0], pos.x + move[1]]
  )

def part_a():
  bottomRightCorner = Point([len(input_data_matrix) -1, len(input_data_matrix[0]) - 1])
  target = Point([len(input_data_matrix) -1, len(input_data_matrix[0]) - 2])

  print("part 1: \n")
  print(input_data)
  print(f"\nstart: {START}")
  print(f"target: {target}", end="\n\n")

  blizzards = [Blizzard(v, [row, col]) for row, col, v in sum([
      [[row, col, v] for col,v in enumerate(cols)]
      for row, cols in enumerate(input_data_matrix)
    ], []) if v in MOVE_EXPRESSION]

  current = Point(START)
  offset = 0
  stopped = False

  moves = [*MOVES, [0, 0]]
  move_names = [*MOVE_NAMINGS, "waiting"]

  while(stopped is False):
    _ = list(map(lambda blizzard: blizzard.moving(bottomRightCorner), blizzards))
    print(f"{OKBLUE}check {current}{ENDC}")
    for mIdx, move in enumerate(moves):
      possible_pos = moving(current, move)
      print(f"{HEADER}is {move_names[mIdx]}: {possible_pos} possible?{ENDC}")

      if onBounds(possible_pos, bottomRightCorner) and onTarget(possible_pos, target) == False:
        print(f"{FAIL}NO!{ENDC} - \ton bounds", end="\n\n")
        continue

      if onAnyBlizzard(possible_pos, blizzards):
        print(f"{FAIL}NO!{ENDC} - \tis there where one blizzard is see #blizzards", end="\n\n")
        continue

      print(f"{OKGREEN}move {move_names[mIdx]}[{mIdx}] {move}{ENDC} to {possible_pos}\ton offset {offset+1}", end="\n\n")
      current = possible_pos
      break
    stopped = True if onTarget(current, target) else False
    offset += 1

  print(f"\ncurrent offset: {OKGREEN}{offset}{ENDC}")
  return offset


def part_b():
  print("part 2")
  print(puzzle.input_data.splitlines())


# test = [0,0]
# blizzards = [Blizzard(v, [row, col]) for row, col, v in sum([
#     [[row, col, v] for col,v in enumerate(cols)]
#     for row, cols in enumerate(input_data_matrix)
#   ], []) if v in MOVE_EXPRESSION]

# print(f"\n\n{HEADER}show blizzard points:\n{[blizzard.pos for blizzard in blizzards]}{ENDC}")
# _ = list(map(lambda blizzard: blizzard.moving(Point([5,7])), blizzards))

# print(f"\n\n{HEADER}show blizzard points:\n{[blizzard.pos for blizzard in blizzards]}{ENDC}")
# print(test in blizzards, blizzards)

# stopped = False
# l = range(100)
# offset = 0
# while stopped == False:
#   for i in l:
#     print(i)
#     if i == 50:
#       print("break")
#       break
#   offset += 1
#   stopped = True if offset > 100 else False
#   print(stopped, offset)

visitied = set()

visitied.add((0, 1))

print((0, 2) in visitied)


# print(part_a())