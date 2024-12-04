import re

def number_strings_to_list(string) -> list:
  return [int(m.group(0)) for m in re.finditer("(\d+)", string)]

def get_beated_records(timeAndRecordPair):
  beatRecords = 0
  time, record = timeAndRecordPair
  for i, ms in enumerate(range(1, time)):
    distance = (timeAndRecordPair[0] - ms) * ms
    if distance > record:
      beatRecords += 1

  return beatRecords

with open("./inputs/6/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]
  times = number_strings_to_list(lines.pop(0))
  records = number_strings_to_list(lines.pop(0))

  # Part 1
  timeAndRecordPairs = zip(times, records)
  beatedRecords1 = map(get_beated_records, timeAndRecordPairs)

  marginOrErrors = 1
  for beatedRecord in beatedRecords1:
    marginOrErrors *= beatedRecord

  # Part 2
  time = int(''.join(map(str,times)))
  record = int(''.join(map(str,records)))
  beatedRecords2 = get_beated_records((time, record))

  print(f'Part 1: {marginOrErrors}')
  print(f'Part 2: {beatedRecords2}')


