import re

def find_digits_near(position, line):
  return [found for (pos, found) in enumerate(line) if pos >= position - 1 and pos <= position + 1 and found.isdigit()]

def find_between(positions, options):
  start, end = positions
  char, check, lines, row = options
  if row > len(lines)-1 or row < 0:
    return []

  line = lines[row]
  return [((row, pos), found) for (pos, found) in enumerate(line) if pos >= start - 1 and pos <= end and (found == char) == check]

def find_on(positions, options):
  start, end = positions
  char, check, lines, row = options
  line = lines[row]
  return [((row, pos), found) for (pos, found) in enumerate(line) if (pos == start-1 or pos == end) and (found == char) == check]

with open("./inputs/3/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]
  numbers = []
  gears = 1

  options = (".", False, lines)
  gear_adjacents_by_positions = dict()
  for row, line in enumerate(lines):
    for m in re.finditer("(\d+)", line):
      number_adjacents = []
      positions = (m.start(), m.end())

      number_adjacents_above = find_between(positions, (*options, row-1))
      number_adjacents_lr = find_on(positions, (*options, row))
      number_adjacents_below = find_between(positions, (*options, row+1))

      number_adjacents.append(len(number_adjacents_above))
      number_adjacents.append(len(number_adjacents_below))
      number_adjacents.append(len(number_adjacents_lr))

      if sum(number_adjacents) > 0:
        number = int(m.group(0))
        numbers.append(number)
        gear_adjacents = [
          *[(*adj[0], number) for adj in number_adjacents_above if adj[1] == "*"],
          *[(*adj[0], number) for adj in number_adjacents_lr if adj[1] == "*"],
          *[(*adj[0], number) for adj in number_adjacents_below if adj[1] == "*"],
        ]
        # print(row, gear_adjacents)
        for gear_adjacent in gear_adjacents:
          r = gear_adjacent[0]
          c = gear_adjacent[1]

          row_dict = gear_adjacents_by_positions.get(r, {})
          col_list = row_dict.get(c, [])
          col_list.append(number)

          row_dict.update({c: col_list})
          gear_adjacents_by_positions.update({r: row_dict})

  gear_ratios = []
  for gear_adjacents in gear_adjacents_by_positions.values():
    for gear_adjacent_numbers in gear_adjacents.values():
      if len(gear_adjacent_numbers) == 2:
        gear_ratio = 1
        for gear_adjacent_number in gear_adjacent_numbers:
          gear_ratio *= gear_adjacent_number
        gear_ratios.append(gear_ratio)

  print(f'Part 1: {sum(numbers)}')
  print(f'Part 2: {sum(gear_ratios)}')


