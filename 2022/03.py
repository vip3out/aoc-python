import os
import string
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/03.txt"
)

summ1 = summ2 = 0
all_letters = [*string.ascii_lowercase, *string.ascii_uppercase]

with open(input_filepath, encoding = 'utf-8') as f:
  rucksacks = [rucksack.strip() for rucksack in f]
  # part 1
  for rucksack in rucksacks:
    rucksack = rucksack.strip()
    length = len(rucksack)//2

    half1, half2= [rucksack[:length], rucksack[length:]]
    founds1 = [f for f in half1 if f in half2]
    summ1 += all_letters.index(founds1[0]) + 1

  # part 2
  groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
  for group in groups:
    r1, r2, r3 = group
    founds2 = [f for f in r1 if f in r2 and f in r3]
    summ2 += all_letters.index(founds2[0]) + 1

print("part 1: %d" % summ1)
print("part 2: %d" % summ2)

