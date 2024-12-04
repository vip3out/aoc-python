from collections import Counter

cards = "23456789TJQKA"

def getPointsFromHand(item):
  return (item.get("points", 0), *map(cards.index, item.get("hand")))

def getPointsFromHandAndBid(handAndBid):
  hand = handAndBid.get("hand")
  points = max(Counter(hand).values()) - len(set(hand))
  handAndBid.update({"points": points})
  return handAndBid

with open("./inputs/7/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]
  handsAndBids = [tuple(line.split(" ")) for line in lines]

  sortedHandsBidsAndPoints1 = sorted(
    (
      max(Counter(hand).values()) - len(set(hand)),
      *map("23456789TJQKA".index, hand),
      int(bid),
    )
    for hand, bid in handsAndBids
  )

  sortedHandsBidsAndPoints2 = sorted(
    (
      max(0, 0, *map(hand.count, set(hand) - {"J"})) + hand.count("J"),
      -max(1, len(set(hand) - {"J"})),
      *map("J23456789TQKA".index, hand),
      int(bid),
    )
    for hand, bid in handsAndBids
  )

  part1Sum = sum(
    map(
      lambda x: (x[0]+1) * x[1][-1],
      enumerate(sortedHandsBidsAndPoints1)
    )
  )

  part2Sum = sum(
    map(
      lambda x: (x[0]+1) * x[1][-1],
      enumerate(sortedHandsBidsAndPoints2)
    )
  )

  print(f'Part 1: {part1Sum}')
  print(f'Part 2: {part2Sum}')
