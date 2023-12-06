input_lines = open("data.txt").read().splitlines()

sum = 0

for line in input_lines:
    char_values = list(line.encode("ascii"))
    # Track how many bytes the unescaped string will use
    byte_count = 0

    # Use an index as a read pointer to a point in the list
    ptr = 0
    string_length = len(line)

    ascii = list(line.encode("ascii"))
    while ptr < string_length:
        # Check for a \ or " character (ASCII 92)
        if ascii[ptr] == 92 or ascii[ptr] == 34:
            byte_count += 2
        else:
            byte_count += 1
        ptr += 1

    # Add bytes for the enclosing quotes
    byte_count += 2
    sum += byte_count - len(line)

print("Sum: %d" % sum)