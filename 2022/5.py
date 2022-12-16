from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=5)

def buildStacksFromInput(stacks):
  a = int(input_stacks.split("\n")[-1:][0].strip()[-1:])
  l = a * 3 + (a-1)
  stacks = [stack for stack in stacks.split("\n")[:-1]]
  new_stacks = [list() for i in range(a)]
  for stack in stacks:
    new_stack = [item.ljust(l) for item in stack.split("\s")]

    for item in new_stack:
      new_items = [item[i:i+4].strip() for i in range(0, len(item), 4)]
      idx = 0
      for new_item in new_items:
        if new_item:
          new_stacks[idx].append(new_item)
        idx += 1
  return new_stacks

def prepare(stacks, from_stack, quantity, reversed=False):
  stack = [*stacks[from_stack][:quantity]]
  if (reversed == True):
    stack.reverse()
  return stack

def format(stacks):
  return "".join(
    [s[:1][0] for s in stacks]
  ).replace("[", "").replace("]", "")

input_stacks, procedures = puzzle.input_data.split("\n\n")
procedures = procedures.split("\n")

def part_a():
  origin_stacks = buildStacksFromInput(input_stacks)
  new_stacks = origin_stacks
  for procedure in procedures:
    quantity, from_stack, to_stack = [int(s) for s in procedure.split() if s.isdigit()]

    stack = prepare(new_stacks, from_stack-1, quantity, True)
    new_stacks[to_stack-1] = [*stack ,*new_stacks[to_stack-1]]
    new_stacks[from_stack-1] = [*new_stacks[from_stack-1][quantity:]]

  return format(new_stacks)

def part_b():
  origin_stacks = buildStacksFromInput(input_stacks)
  new_stacks = origin_stacks

  for procedure in procedures:
    quantity, from_stack, to_stack = [int(s) for s in procedure.split() if s.isdigit()]

    stack = prepare(new_stacks, from_stack-1, quantity)
    new_stacks[to_stack-1] = [*stack ,*new_stacks[to_stack-1]]
    new_stacks[from_stack-1] = [*new_stacks[from_stack-1][quantity:]]

  return format(new_stacks)