def nextValue(numbers):
  if all(n == 0 for n in numbers):
    return 0

  temp = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
  return numbers[-1] + nextValue(temp)

def prevValue(numbers):
  if all(n == 0 for n in numbers):
    return 0

  temp = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
  return numbers[0] - prevValue(temp)

with open("./inputs/9/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]
  history_lines = [[int(num) for num in line.split()] for line in lines]

  sum_of_predictions_forward = sum(
    list(
      map(nextValue, history_lines)
    )
  )

  sum_of_predictions_backwards = sum(
    list(
      map(prevValue, history_lines)
    )
  )

  print(f'Part 1: {sum_of_predictions_forward}')
  print(f'Part 2: {sum_of_predictions_backwards}')
