from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=23)
import time

NORTH = [
  [-1, 0],
  [-1, 1],
  [-1, -1]
]

WEST = [
  [0, -1],
  [-1, -1],
  [1, -1]
]

EAST = [[row[0], abs(row[1])] for row in WEST]
SOUTH = [[abs(row[0]), row[1]] for row in NORTH]

ELF_CHAR = "#"
GROUND_CHAR = "•"

def getDirection(elf, elfs, order):
  possible_neighbours = []
  possibles = []
  for direction in order:
    possible = []
    for move in direction:
      pos = [elf[0] + move[0], elf[1] + move[1]]
      possible_neighbours.append(pos)
      possible.append(pos)
    possibles.append(possible)

  neighbours = [neighbour for neighbour in possible_neighbours if neighbour in elfs]
  if len(neighbours) == 0:
    return None;

  for idx, possible in enumerate(possibles):
    possible = [move for move in possible if move not in elfs]
    if len(possible) == 3:
      return order[idx][0]
  return None

def getElfsFromMaze(maze):
  elfs_from_maze = []
  for row, cols in enumerate(maze):
    for col, v in enumerate(cols):
      if v == ELF_CHAR:
        elfs_from_maze.append([row, col])
  return elfs_from_maze

def setNewElfsPositions(current_elfs, current_directions):
  proposed_elfs = []
  cached_elfs = [elf for elf in current_elfs]
  for i, elf in enumerate(current_elfs):
    direction = getDirection(elf, current_elfs, current_directions)
    direction = direction if direction != None else [0, 0]

    proposed_elfs.append([elf[0] + direction[0], elf[1] + direction[1]])

  for idx, proposed_pos in enumerate(proposed_elfs):
    current_elfs[idx] = proposed_pos if proposed_elfs.count(proposed_pos) == 1 else current_elfs[idx]

  moving = len([moved_elf for idx,moved_elf in enumerate(current_elfs) if moved_elf != cached_elfs[idx]])
  return [current_elfs, moving]

class Maze:
  def __init__(self, maze_input):
    self.data = []
    self.elfs = []
    for row, cols in enumerate(maze_input):
      row = []
      for col, v in enumerate(cols):
        row.append(v)
        if v == ELF_CHAR:
          self.elfs.append([row, col])
      self.data.append(row)

def part_a():
  max_rounds = 10
  directions = [NORTH, SOUTH, WEST, EAST]
  elfs = getElfsFromMaze(
    [list(line) for line in puzzle.input_data.splitlines()]
  )

  while(max_rounds > 0):
    max_rounds -= 1
    elfs, moving = setNewElfsPositions(elfs, directions)
    max_rounds = 0 if moving == 0 else max_rounds
    directions = [*directions[1:], directions[0]]

  boundaries = [0, 0, 0, 0]
  for elf in elfs:
    boundaries[0] = elf[0] if elf[0] < boundaries[0] else boundaries[0]
    boundaries[1] = elf[0] if elf[0] > boundaries[1] else boundaries[1]
    boundaries[2] = elf[1] if elf[1] < boundaries[2] else boundaries[2]
    boundaries[3] = elf[1] if elf[1] > boundaries[3] else boundaries[3]

  grounds = (boundaries[1] + abs(boundaries[0]) + 1) * (boundaries[3] + abs(boundaries[2]) + 1)
  return grounds - len(elfs)

def part_b():
  start_time = time.time()
  current_round = 1
  directions = [NORTH, SOUTH, WEST, EAST]
  elfs = getElfsFromMaze(
    [list(line) for line in puzzle.input_data.splitlines()]
  )

  while(True):
    start_time_round = time.time()
    elfs, moving = setNewElfsPositions(elfs, directions)


    moving_progress = "".ljust(int(moving / len(elfs) * 100), ELF_CHAR).ljust(100, GROUND_CHAR)
    moving_expression = str(moving).zfill(len(list(str(len(elfs)))))
    time_round_seconds = round(time.time() - start_time_round, 2)
    total_time = round((time.time() - start_time) / 60, 2)


    print("Current Round: %i |%s|(moving: %s) [time for round: %fsec - total time: %fmin" % (current_round, moving_progress, moving_expression, time_round_seconds, total_time), end="\r")

    if moving == 0:
      return current_round

    directions = [*directions[1:], directions[0]]
    current_round += 1