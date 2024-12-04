import re
from operator import mul
from functools import reduce

class Game:
  def __init__(self, instruction) -> None:
    m = re.search("Game (\d+)\: (.*)", instruction)
    self.uuid = int(m.group(1))
    self.resolveSubsets(m.group(2))
    pass

  def resolveSubsets(self, cubeInstruction):
    # self.cubes = dict({'red': 0, 'blue': 0, 'green': 0})
    self.subsets = []
    subsets = [subset.split(", ") for subset in cubeInstruction.split("; ")]
    for subset in subsets:
        cube = dict({'red': 0, 'blue': 0, 'green': 0})
        for color in subset:
          colorInstruction = color.split(" ")[::-1]
          colorCount = cube.get(colorInstruction[0])
          colorCount += int(colorInstruction[1])
          cube.update([[colorInstruction[0], colorCount]])
        self.subsets.append(cube)

  def highest_color_cube_subset(self):
    highest_color_cube_subset = dict({'red': 0, 'blue': 0, 'green': 0})
    for subset in self.subsets:
      for key in subset.keys():
        highest_color_cube_subset[key] = highest_color_cube_subset[key] if subset[key] <= highest_color_cube_subset[key] else subset[key]
    return highest_color_cube_subset

  def check(self, max_cubes):
    valid = True
    for subset in self.subsets:
      for key in max_cubes.keys():
        valid = subset.get(key) <= max_cubes.get(key) if valid == True else False
    return valid

with open("./inputs/2/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]
  games = [Game(line) for line in lines]
  max_cubes = dict({'red': 12, 'blue': 14, 'green': 13})
  # for game in games:
  #   print(game.highest_color_cube_subset())

  possible_games = [game for game in games if game.check(max_cubes)]
  highest_color_cubes_counts = [reduce(mul, counts) for counts in [count for count in [game.highest_color_cube_subset().values() for game in games]]]
  # print([p.uuid for p in possible_games])
  print(f'Part 1: {sum([p.uuid for p in possible_games])}')
  print(f'Part 2: {sum(highest_color_cubes_counts)}')