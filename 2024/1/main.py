from modules.helper import open_and_readlines

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


example_file_path = "1/example.txt"
input_file_path = "1/input.txt"

input = open_and_readlines(example_file_path)

data = [tuple(line.split()) for line in input]
data = list(zip(*data))
data = [tuple(map(int, l)) for l in data]

print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")