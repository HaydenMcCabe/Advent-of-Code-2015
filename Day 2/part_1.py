import sys

input = open("data.txt").read().splitlines()
sum = 0

for dimensions in input:
    parts = dimensions.split("x")
    l = int(parts[0])
    w = int(parts[1])
    h = int(parts[2])

    top = l * w
    front = w * h
    side = h * l

    smallest = min(min(top, front), side)
    area = 2 * top + 2 * front + 2 * side + smallest
    sum += area

print(sum)