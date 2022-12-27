from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=17)

until = 2022

rock_index = 0
pattern_index = 0
current_bottom_offset = 0

pattern = list(puzzle.example_data)
rocks = [rock.split("\n") for rock in '''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''.split("\n\n")]

class Rock:
  def __init__(self, data):
    self.rows = len(data)
    self.cols = len(data[-1])
    self.

# print(rocks)
counter = 0
while(counter < until):
  rock_index = (counter + 1) - int((counter + 1) / 5) * 5
  current_rock = Rock(rocks[rock_index])
  # if (current_rock.space.bottom == 0):
  print(rock_index, current_rock.rows, current_rock.cols)

  counter += 1


def part_a():
  print("part 1")
  print(puzzle.input_data.splitlines())

def part_b():
  print("part 2")
  print(puzzle.input_data.splitlines())

