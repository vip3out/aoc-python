import os
import re
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/05.txt"
)

current_stacks = current_stacks1 = current_stacks2 = []

# def part_fn(c, f, t, q, reverse=True):
#     res = [*c]
#     stack = [*res[f][:q]]
#     if reverse:
#       stack.reverse()
#     res[t] = [*stack ,*res[]]
#     res[f] = [*res[f][q:]]
#     return c

with open(input_filepath, encoding = 'utf-8') as f:
  content = f.read()

  stacks, procedures = content.split("\n\n")
  a = int(stacks.split("\n")[-1:][0][-1:])
  l = a * 3 + (a-1)
  stacks = [stack for stack in stacks.split("\n")[:-1]]
  current_stacks = [list() for i in range(a)]
  for stack in stacks:
    stack1 = [s.ljust(l) for s in stack.split("\s")]
    # print(stack1)
    for s1 in stack1:
      s2 = [s1[i:i+4].strip() for i in range(0, len(s1), 4)]
      idx = 0
      for s3 in s2:
        if s3:
          current_stacks[idx].append(s3)
        idx += 1

  procedures = procedures.split("\n")
  for procedure in procedures:
    quantity, from_stack, to_stack = [int(s) for s in procedure.split() if s.isdigit()]

    stack = [*current_stacks[from_stack-1][:quantity]]
    # stack.reverse() #comment out for part #2

    current_stacks[to_stack-1] = [*stack ,*current_stacks[to_stack-1]]
    current_stacks[from_stack-1] = [*current_stacks[from_stack-1][quantity:]]



  # print("".join([s[:1][0] for s in current_stacks1]).replace("[", "").replace("]", ""))
  # print("".join([s[:1][0] for s in current_stacks2]).replace("[", "").replace("]", ""))
  print(
    "".join([s[:1][0] for s in current_stacks])
      .replace("[", "")
      .replace("]", "")
  )