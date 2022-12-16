import os
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/01.txt"
)

index = 0
sums = [0]

with open(input_filepath, encoding = 'utf-8') as f:
  for snack in f:
    snack = snack.strip() # strip for hidden empty chars

    if not snack:
      index += 1
      sums.append(0)
    else:
      sums[index] += int(snack)

sums.sort(reverse=True)

print("part 1: %d" % sums[0])
print("part 2: %d" % sum(sums[:3]))