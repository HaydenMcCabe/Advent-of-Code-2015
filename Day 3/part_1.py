import sys

input = open("data.txt").read()

pos_x = 0
pos_y = 0

visits = {(0, 0)}

for c in input:
    if c == "^":
        pos_y += 1
    elif c == "v":
        pos_y -= 1
    elif c == "<":
        pos_x -= 1
    elif c == ">":
        pos_x += 1

    visits.add((pos_x, pos_y))

print(len(visits))