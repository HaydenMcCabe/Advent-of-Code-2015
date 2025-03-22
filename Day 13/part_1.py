import re

input_lines = open("test_data.txt").read().splitlines()
people: {str:{str:int}} = {}
input_regex = re.compile("(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.")
for line in input_lines:
    parts = input_regex.match(line)
    subject = parts.group(1)
    points = (1 if parts.group(2) == "gain" else -1) * int(parts.group(3))
    other = parts.group(4)
    if (relationships := people.get(subject, None)) is not None:
        relationships[other] = points
    else:
        people[subject] = {other:points}
print(people)