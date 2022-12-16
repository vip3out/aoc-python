import os
input_filepath = os.path.join(
  os.path.dirname(__file__),
  "input/02.txt"
)

score1 = score2 = 0

# A = ROCK, B = PAPER, C = SCISSOR
oppenent =  ["A","B","C"]

# part 1
# X = A (ROCK), Y = B (PAPER), Z = C (SCISSOR)
# => A vs Y == win  ==> 6 + 2
# => B vs X == lose ==> 0 + 1
# => C vs Z == draw ==> 3 + 3
# ==> 15
#
# => B(1) vs Y(1) == draw (0)
# => A(0) vs Y(1) == win (-1)
# => B(1) vs Z(2) == win (-1)
# => C(2) vs X(0) == win (2)
p1 = ["X","Y","Z"] # part1
wins1 = [-1, 2]

# part 2
# X = lose, Y = draw, Z = win
# => A vs Y == draw ==> 3 + 1
# => B vs X == lose ==> 0 + 1
# => C vs Z == win  ==> 6 + 1
# ==> 12
#
# => A(0) vs X(lose)(0) => A : X -> Z [2] (0) 0
# => A(0) vs Y(draw)(1) => A : Y -> X [2] (3) -1
# => A(0) vs Z(win)(2)  => A : Z -> Y [2] (6) -2 x
#
# => B(1) vs X(lose)(0) => B : X -> X [0] (0) 1
# => B(1) vs Y(draw)(1) => B : Y -> Y [0] (3) 0
# => B(1) vs Z(win)(2)  => B : Z -> Z [0] (6) -1 x

# => C(2) vs X(lose)(0) == Y (0) 2
# => C(2) vs Y(draw)(1) == Z (3) 1
# => C(2) vs Z(win)(2)  == X (6) 0 x

with open(input_filepath, encoding = 'utf-8') as f:
  for g in f:
    a, b = g.strip().split(" ")
    p1x = p1.index(b)

    r1 = oppenent.index(a) - p1x
    v1 = 6 if r1 in wins1 else 3 if r1 == 0 else 0
    score1 += p1x + 1 + v1

    trans_op = (oppenent.index(a) + 2) % 3
    selected_index = (p1x + trans_op) % 3
    v2 = 6 if p1x > 1 else 3 if p1x == 1 else 0
    score2 += selected_index + 1 + v2

print("part 1: %d" % score1)
print("part 2: %d" % score2)