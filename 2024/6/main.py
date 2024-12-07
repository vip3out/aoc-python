from modules.helper import open_and_readlines, cycle, transform_list, print_progress
from math import floor
import numpy as np

GUARD_DIRECTION_KEYS = "^>v<"
GUARD_DIRECTIONS = [[-1,0], [0,1], [1,0], [0,-1]]

def get_output_of_map(m):
  output = ""
  for row in m:
    for col in row:
      output += col
    output += "\n"

  return output

def get_visited_position(m):
  return [(row, col) for row, line in enumerate(m) for col, v in enumerate(line) if v in "X"]

def get_guard(m):
  row = [r for r, l in enumerate(m) if any(map(lambda g: g in GUARD_DIRECTION_KEYS, l))][0]
  col = [c for c, g in enumerate(m[row]) if g in GUARD_DIRECTION_KEYS][0]

  return (
    [row, col],
    cycle(
      transform_list(
        GUARD_DIRECTIONS,
        GUARD_DIRECTION_KEYS.index(m[row][col])
      )
    ),
    m[row][col]
  )

def pos_is_in_map(pos, m):
  return all([
    pos[0] > 0,
    pos[1] > 0,
    len(m) - pos[0] > 1,
    len(m) - pos[1] > 1,
  ])

def move_until_next_obstacle(m, pos, direction, pointer, guard_pointer):
  while pos_is_in_map(pos, m):
    pos[0], pos[1] = pos[0] + direction[0], pos[1] + direction[1]
    if m[pos[0]][pos[1]] == "#": return [pos[0] - direction[0], pos[1] - direction[1]], m, False
    if m[pos[0]][pos[1]] == "O": return [pos[0] - direction[0], pos[1] - direction[1]], m, True

    if m[pos[0]][pos[1]] != guard_pointer:
      m[pos[0]][pos[1]] = pointer[0] if direction[0] == 0 else pointer[1]
  return pos, m, False

def guard_moving(m, pointer, check_for_loop = False):
  guard_pos, guard_directions, guard_pointer = get_guard(m)

  positions_of_direction_change = []
  guard_directions = cycle(GUARD_DIRECTIONS)
  current_length = 0
  in_loop = False
  visited_my_obstacle = False
  while pos_is_in_map(guard_pos, m):
    guard_pos, m, visit_my_obstacle = move_until_next_obstacle(
      m,
      guard_pos,
      next(guard_directions),
      pointer[:2],
      guard_pointer
    )

    visited_my_obstacle = visit_my_obstacle if visited_my_obstacle == False else visited_my_obstacle

    if check_for_loop and visited_my_obstacle == True:
      current_length = len(positions_of_direction_change)
      if current_length > 4 and (guard_pos[0], guard_pos[1]) in positions_of_direction_change[:-1]:
        in_loop = True
        break

    positions_of_direction_change.append((guard_pos[0], guard_pos[1]))
    if m[guard_pos[0]][guard_pos[1]] != guard_pointer:
      m[guard_pos[0]][guard_pos[1]] = pointer[2]

  return m, in_loop

def part_one(input):
  labmap = [list(line) for line in input]
  labmap, _ = guard_moving(labmap, "XXX")
  visited_positions = get_visited_position(labmap)

  return len(visited_positions)

def part_two(input):
  labmap = [list(line) for line in input]
  labmap, _ = guard_moving(labmap, "XXX")
  visited_positions = get_visited_position(labmap)

  loop_posibilities = 0
  for i, visited_position in enumerate(visited_positions):
    new_labmap = [list(line) for line in input]
    new_labmap[visited_position[0]][visited_position[1]] = "O"
    new_labmap, in_loop = guard_moving(new_labmap, "-|+", True)
    loop_posibilities += 1 if in_loop == True else 0
    print_progress(i, len(visited_positions), True)

  print_progress(len(visited_positions), len(visited_positions))
  return loop_posibilities


example_file_path = "6/example.txt"
input_file_path = "6/input.txt"

input = open_and_readlines(input_file_path)
print(f"Part 1: {part_one(input)}")
print(f"Part 2: {part_two(input)}")