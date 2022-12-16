import os
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/04.txt"
)

# bring sections into an array: 2-4, 6-8 -> 2,3,4 and 6,7,8
# then check if the smallest or equal length array has all items are in the longer or equal length an array

# 2-4 -> split and extract
# a:2, b:4 -> = range(a, b+1)
# smoreq = sections_a if len(sections_a) <=len(sections_b) else sections_b
# founds = [section for section in smoreg if section in sections_b]

# part 1
# counts += 1 if len(founds) == len(smoreq) else 0

# part 2
# counts += 1 if len(founds) > 0 else 0

count1 = count2 = 0

with open(input_filepath, encoding = 'utf-8') as f:
  pairs = [pair.strip().split(",") for pair in f]
  for pair in pairs:
    section_a, section_b = sorted(
      [
        list(range(int(a), int(b)+1)) for a,b in [
          section.split("-") for section in pair
        ]
      ],
      key=len
    )
    founds = [found for found in section_a if found in section_b]

    count1 += 1 if len(founds) == len(section_a) else 0
    count2 += 1 if len(founds) > 0 else 0

print(f"part 1: {count1}")
print(f"part 2: {count2}")
