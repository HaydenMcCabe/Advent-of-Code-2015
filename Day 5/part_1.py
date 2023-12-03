import re

input = open("data.txt").read().splitlines()

vowel_regex = re.compile("[aeiou]")
double_regex = re.compile(r"(.)\1")
bad_matches = re.compile("(ab|cd|pq|xy)")

nice_count = 0

for line in input:
    vowel_count = len(vowel_regex.findall(line))
    double_match = double_regex.search(line) != None
    no_bad_matches = bad_matches.search(line) == None
    if vowel_count >= 3 and double_match and no_bad_matches:
        nice_count += 1

print(nice_count)
