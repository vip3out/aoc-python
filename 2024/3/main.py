import re
from functools import reduce
from modules.helper import open_and_concatlines

def do_operations(memory):
  p = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
  ops = p.findall(memory)
  products = [reduce(lambda x,y: int(x)*int(y), re.findall(r"\d{1,3}", op)) for op in ops]
  return products

def part_one(memory):
  products = do_operations(memory)
  return sum(products)

def part_two(memory):
  clean = re.sub(r"don\'t\(\)[\s\S]*?(do\(\)|$)", "", memory)
  products = do_operations(clean)

  return sum(products)

example_file_path = "3/example.txt"
input_file_path = "3/input.txt"

input = open_and_concatlines(input_file_path)
print(f"Part 1: {part_one(input)}")
print(f"Part 2: {part_two(input)}")