
from modules.helper import open_and_readlines, print_progress
from itertools import product
from operator import mul, add

def get_equation_vars(line):
  test, operands = line.split(": ")
  combined = list(map(int, [test] + operands.split(" ")))
  return combined[0], combined[1:]

def equation(operands: list[int], ops: list[callable]):
  if (len(operands) == 1):
    return operands[0]

  l, r, *rest = operands
  cur_op, *next_ops = ops

  match cur_op:
    case "||":
      cur_op_result = int(str(l) + str(r))
    case _:
      cur_op_result = cur_op(l, r)

  return equation([cur_op_result, *rest], next_ops)

def process(input, operators):
  result = 0

  for cur, line in enumerate(input):
    test, operands = get_equation_vars(line)
    equations = product(operators, repeat=len(operands) - 1)
    solutions = []
    for op_combo in equations:
      solutions.append(equation(operands, op_combo))

    print_progress(cur, len(input), True)

    if any(
      map(lambda result: result == test, solutions)
    ):
      result += test

  print_progress(len(input), len(input))
  return result

def part_one(input):
  return process(input, [add, mul])

def part_two(input):
  return process(input, [add, mul, "||"])


example_file_path = "7/example.txt"
input_file_path = "7/input.txt"

input = open_and_readlines(input_file_path)
print(f"Part 1: {part_one(input)}")
print(f"Part 2: {part_two(input)}")