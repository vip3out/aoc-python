import re

with open("./inputs/4/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]
  points = 0
  copy_cards = []
  for line in lines:
    card_instruction, all_numbers = line.split(": ")
    winning_numbers, numbers = all_numbers.split(" | ")
    _, card = [i for i in card_instruction.split(" ") if i != '']
    card = int(card)

    winning_numbers = [int(m.group(0)) for m in list(re.finditer("(\d+)", winning_numbers))]
    numbers = [int(m.group(0)) for m in list(re.finditer("(\d+)", numbers))]

    count_winnings = len(set(winning_numbers) & set(numbers))

    line_points = 0
    copy_cards.append(card)
    current = card
    if count_winnings > 0:
      copy_cards_of_current = [c for c in copy_cards if c == current]
      for i, _ in enumerate(copy_cards_of_current):
        card = current
        for z in range(count_winnings):
          card += 1
          copy_cards.append(card)

      line_points += 1
      for i in range(count_winnings-1):
        line_points *= 2

    points += line_points

  unique_copy_cards = set(copy_cards)
  print(f'Part 1: {points}')
  print(f'Part 2: {sum([copy_cards.count(u) for u in unique_copy_cards])}')


