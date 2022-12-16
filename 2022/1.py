from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=1)

def calculate_sum_of_snacks(snacks):
  index = 0
  sums = [0]
  for snack in snacks:
    snack = snack.strip() # strip for hidden empty chars

    if not snack:
      index += 1
      sums.append(0)
    else:
      sums[index] += int(snack)

  sums.sort(reverse=True)
  return sums


def part_a():
  sums = calculate_sum_of_snacks(
    puzzle.input_data.splitlines()
  )
  return sums[0]

def part_b():
  sums = calculate_sum_of_snacks(
    puzzle.input_data.splitlines()
  )
  return sum(sums[:3])

