import sys

input = open("data.txt").read().splitlines()
#input = ["2x3x4", "1x1x10", "23x11x5"]
sum = 0

for dimensions in input:
    # Find the two smallest dimentions
    parts = dimensions.split("x")
    sorted = list(map(int, parts))
    sorted.sort()
    perimeter = 2 * (sorted[0] + sorted[1])
    length = perimeter + (sorted[0] * sorted[1] * sorted[2])
    print("%s : %d ; %d" % (dimensions, perimeter, length))
    print(parts)
    print("\n")
    sum += length
    
print(sum)