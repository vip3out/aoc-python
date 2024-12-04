import re

def batched(l, size):
  n = max(1, size)
  return [l[i:i+n] for i in range(0, len(l), n)]

def number_strings_to_list(string) -> list:
  return [int(m.group(0)) for m in re.finditer("(\d+)", string)]

def resolve_map_block(map_block):
  print(f'resolve {map_block.pop(0).replace(":", "")} block')
  return [number_strings_to_list(op) for op in map_block]

def get_flow_from_map_blocks(current, map_blocks):
  flow = [current]
  value = current

  for map_block in map_blocks:
    for op in map_block:
      if value >= op[1] and value < op[1] + op[2]:
        diff = value - op[1]
        value = op[0] + diff
        break
    flow.append(value)
  return flow

def get_locations_from_seeds(seeds, map_blocks, hasSeedLength = False):
  smallest_location = 1111111111111111
  if hasSeedLength == True:

    for batch_seeds in batched(seeds, 2):
      start = batch_seeds[0]
      length = batch_seeds[1]

      for value in list(range(start, start + length)):
        seed_to_location_flow = get_flow_from_map_blocks(value, map_blocks)
        location = seed_to_location_flow[-1]
        if location < smallest_location:
          smallest_location = location
    return smallest_location

  for value in seeds:
    seed_to_location_flow = get_flow_from_map_blocks(value, map_blocks)
    location = seed_to_location_flow[-1]
    if location < smallest_location:
      smallest_location = location
  return smallest_location

with open("./inputs/5/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]

  maps = dict()
  current_map_dict = dict()

  seed_line = lines.pop(0)

  seeds = number_strings_to_list(seed_line.replace("seeds: ", ""))

  lines.pop(0)

  map_blocks = list()
  map_block_index = -1
  for (index, line) in enumerate(lines):
    if 'map' in line:
      if map_block_index >= 0:
        map_blocks[map_block_index].append(index-1)
      map_block_index += 1
      map_blocks.append([index])

  map_blocks[map_block_index].append(len(lines)-1)
  map_blocks = [resolve_map_block(lines[x[0]:x[1]]) for x in map_blocks]

  locations_1 = get_locations_from_seeds(
    seeds,
    map_blocks
  )

  locations_2 = get_locations_from_seeds(
    seeds,
    map_blocks,
    True
  )

  print(locations_1, locations_2)

  # print(f'Part 1: {min(locations_1)}')
  # print(f'Part 2: {min(locations_2)}')





