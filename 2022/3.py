import string
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=3)
rucksacks = [rucksack.strip() for rucksack in puzzle.input_data.splitlines()]
all_letters = [*string.ascii_lowercase, *string.ascii_uppercase]

def part_a():
  summ = 0
  for rucksack in rucksacks:
    rucksack = rucksack.strip()
    length = len(rucksack)//2

    half1, half2= [rucksack[:length], rucksack[length:]]
    founds = [f for f in half1 if f in half2]
    summ += all_letters.index(founds[0]) + 1

  return summ

def part_b():
  summ = 0
  groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
  for group in groups:
    r1, r2, r3 = group
    founds = [f for f in r1 if f in r2 and f in r3]
    summ += all_letters.index(founds[0]) + 1

  return summ
