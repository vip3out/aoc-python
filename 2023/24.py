import sympy as sy
from sympy.abc import x

area = [7,27]

class Point:
  def __init__(self, positions):
    x, y, z = list(positions)
    self.x = x
    self.y = y
    # self.z = z

  def move(self, velocity):
    vx, vy, vz = velocity
    self.x += vx
    self.y += vy
    # self.z += vz

  def in_area(self, minmax):
    if self.x < minmax[0]:
      return False
    if self.x > minmax[1]:
      return False
    if self.y < minmax[0]:
      return False
    if self.y > minmax[1]:
      return False

    # if self.z < minmax[0]:
    #   return False
    # if self.z > minmax[1]:
    #   return False

    return True


class HailStone:
  # y = mx + t
  def __init__(self, data):
    positions, velocity = [map(int, instruction.split(", ")) for instruction in data.split(" @ ")]
    self.origin = Point(positions)
    self.velocity = tuple(velocity)

  @property
  def path(self):
    path = []
    current = Point(tuple([max(value, area[0]) for value in self.origin]))
    while current.in_area(area):
      path.append(current)
      current.move(self.velocity)

    return path

  @property
  def m(self):
    return self.velocity[1] / self.velocity[0]

  @property
  def t(self):
    return self.m * self.origin.x - self.origin.y

  def intersection(self, hailstone) -> Point:
    #m1 * x1 *
    x1 = sy.solve(
      sy.Eq(
        self.m * x + self.t,
        hailstone.m * x + hailstone.t,
      ),
      x
    )

    print(
      x1, self.m * x1[0] + self.t
    )
    pass




with open("./inputs/24/test.txt") as f:
  lines = [line.strip() for line in f.readlines()]

  hailstones = [HailStone(line) for line in lines]
  while len(hailstones) > 1:
    current = hailstones.pop(0)
    for hailstone in hailstones:
      current.intersection(hailstone)

  print(f'Part 1: ')
  print(f'Part 2: ')
