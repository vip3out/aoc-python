with open("./inputs/25/test.txt") as f:
  lines = [line.strip() for line in f.readlines()]

  wires = dict()
  for line in lines:
    com, other  = line.split(": ")
    other = other.split(" ")

    for oc in other:
      wires[oc] = com

    print(f"for communication instruction on '{com}': {other}")
    print(f"one direction: {wires}\n")

  print(wires.keys())
  print(wires.values())

  print(f'Part 1: ')
  print(f'Part 2: ')



# 9 components: cmg, frs, lhk, lsr, nvd, pzl, qnr, rsh, and rzs.
# 6 components: bvb, hfx, jqt, ntq, rhn, and xhk.