from math import lcm
from itertools import cycle
def prepareElement(element):
  node, lr = element.split(" = ")
  lr = tuple(str(lr[1:-1]).split(", "))
  return (node, lr)

with open("./inputs/8/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]

  instructions = cycle(map("LR".index, lines.pop(0)))
  lines.pop(0)

  nodes, instruction_nodes = list(
    zip(*map(prepareElement, lines))
  )

  def direction_sequence(current_node, endswith):
    cycle_count = 0
    while not current_node.endswith(endswith):
      instruction = next(instructions)
      current_node = instruction_nodes[nodes.index(current_node)][instruction]
      cycle_count += 1
    return cycle_count

  current_node = "AAA"
  cycle_count_1 = direction_sequence("AAA", "ZZZ")
  print(f'Part 1: {cycle_count_1}')

  starting_nodes = [node for node in nodes if node[-1] == "A"]
  counters = []

  for starting_node in starting_nodes:
    counters.append(
      direction_sequence(starting_node, "Z")
    )

  print(f'Part 2: {lcm(*counters)}')
