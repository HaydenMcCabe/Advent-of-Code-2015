import sys

input = open("data.txt").read()

floor = 0
for c in input:
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

print(floor)