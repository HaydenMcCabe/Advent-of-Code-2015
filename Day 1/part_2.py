import sys

input = open("data.txt").read()

floor = 0


for i in range(len(input)):
    c = input[i]
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
    # Check to see if we just went negative
    if floor == -1:
        print(i + 1)
        sys.exit()


print("No basement")