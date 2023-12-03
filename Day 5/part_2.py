import re

input = open("data.txt").read().splitlines()

double_regex = re.compile(r"(..).*\1")
surround_regex = re.compile(r"(.).\1")

nice_count = 0

for line in input:
    double_match = double_regex.search(line) != None
    surround_match = surround_regex.search(line) != None
    if double_match and surround_match:
        nice_count += 1

print(nice_count)
