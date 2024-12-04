pipes = "|-LJF7"

direction_keys = ("DOWN", "RIGHT", "LEFT", "UP")
direction_values = ((1,0), (0,1), (0,-1), (-1,0))
directions = dict(zip(direction_keys, direction_values))
print(directions)

def new_direction(pipe, direction):
  if pipe in "|-":
    return direction

  if pipe == "F" and direction == "LEFT":
    return "DOWN"

  if pipe == "7" and direction == "RIGHT":
    return "DOWN"

  if pipe == "F" and direction == "UP":
    return "RIGHT"

  if pipe == "L" and direction == "DOWN":
    return "RIGHT"

  if pipe == "J" and direction == "DOWN":
    return "LEFT"

  if pipe == "7" and direction == "UP":
    return "LEFT"

  if pipe == "J" and direction == "RIGHT":
    return "UP"

  if pipe == "L" and direction == "LEFT":
    return "UP"

with open("./inputs/10/input.txt") as f:
  lines = [line.strip() for line in f.readlines()]
  maze = [[col for col in list(row)] for row in lines]
  start = [[(r, c)for c, col in enumerate(row) if col == "S"] for r, row in enumerate(maze) if "S" in row][0][0]

  current = 0
  pointer = (start[0], start[1] + 1)
  direction = "RIGHT"

  while maze[pointer[0]][pointer[1]] != "S":
    if maze[pointer[0]][pointer[1]] in pipes:
      pipe = maze[pointer[0]][pointer[1]]
      current += 1
      maze[pointer[0]][pointer[1]] = current
      direction = new_direction(pipe, direction)
      direction_value = directions.get(direction)
      pointer = (
        pointer[0] + direction_value[0],
        pointer[1] + direction_value[1]
      )

  print(maze)
  print(f'Part 1: {int((current + 1) / 2)}')
  print(f'Part 2: ')






