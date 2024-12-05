from math import floor
from functools import reduce
from modules.helper import open_and_split_into_blocks

def swapIndexes(l, aI, bI):
  l[aI], l[bI] = l[bI], l[aI]
  return l

def validate_update(update, rules):
  return reduce(
    lambda valid, i: valid and all(
      map(
        lambda v: v in rules.get(update[i], []),
        update[i+1:]
      )
    ),
    range(len(update)),
    True
  )

def correct_update(update, rules):
  i = 0
  while i < len(update):
    check = list(map(
      lambda v: v in rules.get(update[i], []),
      update[i+1:]
    ))

    if False not in check:
      i += 1
      continue

    incorrect_index = check.index(False)
    update = swapIndexes(update, i, i + incorrect_index + 1)
    i = i
  return update

def part_one(rules, updates):
  valid_updates = [update for update in updates if validate_update(update, rules) == True]

  return sum(
    [update[floor(len(update) / 2)] for update in valid_updates]
  )

def part_two(rules, updates):
  invalid_updates = [update for update in updates if validate_update(update, rules) == False]
  corrected_updates = [correct_update(update, rules) for update in invalid_updates]

  return sum(
    [update[floor(len(update) / 2)] for update in corrected_updates]
  )

example_file_path = "5/example.txt"
input_file_path = "5/input.txt"

rules, updates = open_and_split_into_blocks(input_file_path)

parsed_rules = {}
for rule in rules:
  key_page, page = [int(page) for page in rule.split("|")]
  current_rule_pages = parsed_rules.get(key_page, [])
  current_rule_pages.append(page)
  parsed_rules.update({key_page: current_rule_pages})

updates = [list(map(int, pages.split(","))) for pages in updates]

print(f"Part 1: {part_one(parsed_rules, updates)}")
print(f"Part 2: {part_two(parsed_rules, updates)}")