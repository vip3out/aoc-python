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

START = (0,1)
MOVES = [
  (0, 1),
  (1, 0),
  (-1, 0),
  (0, -1)
]
MOVE_EXPRESSION = list(">v^<")
MOVE_NAMINGS = "rightwards, downwards, upwards, leftwards".split(", ")

input_data = puzzle.input_data
input_data_lines = input_data.splitlines()
input_data_matrix = [list(row) for row in input_data_lines]

def movingBlizzard(blizzard, wallBottomRightCorner):
  currentY, currentX, move_expression = blizzard
  moveY, moveX = MOVES[MOVE_EXPRESSION.index(move_expression)]
  y, x = (currentY + moveY, currentX + moveX)
  cornerY, cornerX = wallBottomRightCorner

  return (
    cornerY - 1 if y == 0 else y if y < cornerY else 1,
    cornerX - 1 if x == 0 else x if x < cornerX else 1,
    move_expression
  )
def onTarget(pos, target):
  y, x = pos
  targetY, targetX = target
  return True if x == targetX and y == targetY else False

def onBoundsOrOutsideValley(pos, wallBottomRightCorner):
  y, x = pos
  cornerY, cornerX = wallBottomRightCorner
  if x <= 0 or y <= 0:
    return True

  if x == cornerX or y == cornerY:
    return True

  return False

def onAnyBlizzard(pos, blizzards):
  return pos in [(blizzardY, blizzardX) for blizzardY, blizzardX, _ in blizzards]

def movingElf(pos, move):
  currentY, currentX = pos
  moveY, moveX = move
  return (currentY + moveY, currentX + moveX)

def calculate_minutes(start, target, blizzards, bottomRightCorner):
  current_positions = set()

  minute = 0
  current_positions.add((*start, minute))

  moves = [*MOVES, (0, 0)]

  while(True):
    if minute % 100 == 0:
      print(f"--- {minute} ---")
    minute += 1
    blizzards = list(map(lambda blizzard: movingBlizzard(blizzard, bottomRightCorner), blizzards))

    previous_positions = [(y,x) for y,x,m in current_positions if m ==  minute - 1]

    for current in previous_positions:
      possibles = [movingElf(current, move) for move in moves]

      if target in possibles:
        return (minute, blizzards)

      valid_positions = [possible for possible in possibles if (current == possible and possible == start) or (onBoundsOrOutsideValley(possible, bottomRightCorner) == False and onAnyBlizzard(possible, blizzards) == False)]

      for valid_position in valid_positions:
        current_positions.add((*valid_position, minute))


def part_a(returningBlizzards = False):
  bottomRightCorner = (len(input_data_matrix) -1, len(input_data_matrix[0]) - 1)
  target = (len(input_data_matrix) -1, len(input_data_matrix[0]) - 2)

  blizzards = [(row, col, v) for row, col, v in sum([
      [[row, col, v] for col,v in enumerate(cols)]
      for row, cols in enumerate(input_data_matrix)
    ], []) if v in MOVE_EXPRESSION]

  print("part 1: \n")
  print(f"\nstart: {START}")
  print(f"target: {target}", end="\n\n")

  result = calculate_minutes(START, target, blizzards, bottomRightCorner)
  print(f"away path takes: {result[0]}", end="\n\n")


  if returningBlizzards:
    return result

  return result[0]

def part_b():
  away_minutes, blizzards = part_a(True)

  bottomRightCorner = (len(input_data_matrix) -1, len(input_data_matrix[0]) - 1)
  start = (len(input_data_matrix) -1, len(input_data_matrix[0]) - 2)
  target = START

  print("part 2: \n")
  print(f"\nstart: {start}")
  print(f"target: {target}", end="\n\n")

  wayback_minutes, blizzards = calculate_minutes(start, target, blizzards, bottomRightCorner)
  print(f"way back path takes: {wayback_minutes}", end="\n\n")

  print(f"\nstart: {target}")
  print(f"target: {start}", end="\n\n")
  away2_minutes, _ = calculate_minutes(target, start, blizzards, bottomRightCorner)
  print(f"away path again takes: {away2_minutes}", end="\n\n")

  return wayback_minutes + away_minutes + away2_minutes