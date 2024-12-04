# from aocd.models import Puzzle
# puzzle = Puzzle(year=2023, day=1)
num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extract_sum_from_nums(line):
  nums = []

  for(c,char) in enumerate(line):
    if char.isdigit() == True:
      nums.append(int(char))

  return int(f'{nums[0]}{nums[-1]}')

def extract_sum_from_nums_with_num_words(line):
  nums = []

  for(c,char) in enumerate(line):
    for (n, num_word) in enumerate(num_words):
      test = f'{line[c:(len(num_word)+c)]}'
      print(test, num_word)
      if test == num_word:
        nums.append(n+1)

    if char.isdigit() == True:
      nums.append(int(char))

  return int(f'{nums[0]}{nums[-1]}')

with open("./inputs/1.txt") as f:
  lines = [line.strip() for line in f.readlines()]
  data = [extract_sum_from_nums_with_num_words(line) for line in lines]

  print(data)
  print(sum(data))

# print(extract_sum_from_nums_with_num_words("threefivethree"))