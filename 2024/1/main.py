from modules.helper import open_and_readlines

lines = open_and_readlines("1/input.txt")
data = [tuple(line.split()) for line in lines]
data = list(zip(*data))
data = [tuple(map(int, l)) for l in data]

def part_one(data):
  data = [tuple(sorted(l)) for l in data]
  distances = list()
  for (i, v) in enumerate(data[0]):
    distances.append(abs(v - data[1][i]))

  return sum(distances)

def part_two(data):
  similarity_scores = list()
  for (i, v) in enumerate(data[0]):
    if v in data[1]:
      similarity_scores.append(v * data[1].count(v))
  return sum(similarity_scores)

print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")