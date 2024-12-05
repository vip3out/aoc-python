from math import floor
from functools import reduce
from modules.helper import open_and_split_into_blocks

def swapIndexes(l, aI, bI):
  l[aI], l[bI] = l[bI], l[aI]
  return l

def parse_updates(updates):
  return [list(map(int, pages.split(","))) for pages in updates]

def parse_rules(rules):
  parsed_rules = {}
  for rule in rules:
    key_page, page = [int(page) for page in rule.split("|")]
    current_rule_pages = parsed_rules.get(key_page, [])
    current_rule_pages.append(page)
    parsed_rules.update({key_page: current_rule_pages})

  return parsed_rules

def middle_page_number_of_update(update):
  middle_key = floor(len(update) / 2)
  return update[middle_key]

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
  middle_page_numbers = []
  for update in updates:
    valid = validate_update(update, rules)
    if valid:
      middle_page_numbers.append(middle_page_number_of_update(update))

  return sum(middle_page_numbers)
def part_two(rules, updates):
  middle_page_numbers = []
  for update in updates:
    valid = validate_update(update, rules)
    if valid == False:
      corrected_update = correct_update(update, rules)
      middle_page_numbers.append(middle_page_number_of_update(corrected_update))

  return sum(middle_page_numbers)

example_file_path = "5/example.txt"
input_file_path = "5/input.txt"

rules, updates = open_and_split_into_blocks(input_file_path)
rules = parse_rules(rules)
updates = parse_updates(updates)

print(f"Part 1: {part_one(rules, updates)}")
print(f"Part 2: {part_two(rules, updates)}")