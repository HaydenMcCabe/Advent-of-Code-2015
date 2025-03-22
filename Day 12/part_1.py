import re

number_regex = re.compile(r"(-?\d+)")

data = open("data.txt").read()

numbers = number_regex.findall(data)
ints = list(map(int, numbers))

sum = 0
for i in range(len(ints)):
    sum += ints[i]

print(sum)
