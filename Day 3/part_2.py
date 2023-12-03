import sys

input = open("data.txt").read()
#input = "^v^v^v^v^v"

positions = [[0,0],[0,0]]
x = 0
y = 1

visits = {(0, 0)}

# Use a number to track whose turn it is
turn_mod = 0

for c in input:
    if turn_mod == 0:
        # Santa's turn
        position_index = 0
    elif turn_mod == 1:
        #Robo-Santa's turn
        position_index = 1
    if c == "^":
        positions[position_index][y] += 1
    elif c == "v":
        positions[position_index][y] -= 1
    elif c == "<":
        positions[position_index][x] -= 1
    elif c == ">":
        positions[position_index][x] += 1

    turn_mod = (turn_mod + 1) % 2

    visits.add((positions[position_index][x], positions[position_index][y]))

print(len(visits))