import re
import sys

# Define a 2-dimensional array of boolean values
size = 1000
lights = [[False for x in range(size)] for y in range(size)]

regex = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

# Load the data
input_lines = open("data.txt").read().splitlines()

for line in input_lines:
    parts = regex.match(line)
    # Create the x and y ranges
    rows = range(int(parts.group(2)), int(parts.group(4)) + 1)
    cols = range(int(parts.group(3)), int(parts.group(5)) + 1)

    # Branch based on the command
    if parts.group(1) == "turn on":
        for row in rows:
            for col in cols:
                lights[row][col] += 1

    elif parts.group(1) == "turn off":
        for row in rows:
            for col in cols:
                lights[row][col] = max(0, lights[row][col] - 1)

    elif parts.group(1) == "toggle":
        for row in rows:
            for col in cols:
                lights[row][col] += 2
    else:
        print("Bad input")
        sys.exit()

# Count up the active lights
sum = 0
for x in range(size):
    for y in range(size):
        sum += lights[x][y]
    
print("Sum: %d" % sum)