input_lines = open("data.txt").read().splitlines()

sum = 0

for line in input_lines:
    char_values = list(line.encode("ascii"))
    # Track how many bytes the unescaped string will use
    byte_count = 0

    # Use an index as a read pointer to a point in the list
    # Offset the start position and end position by 1 to
    # account for the enclosing " characters
    ptr = 1
    string_length = len(line) - 1

    ascii = list(line.encode("ascii"))
    while ptr < string_length:
        # Check for a \ character (ASCII 92)
        if ascii[ptr] == 92:
            # Check for the \\ and \" cases
            if ptr + 1 < string_length:
                next_char = ascii[ptr + 1]
                if next_char == 92 or next_char == 34:
                    byte_count += 1
                    ptr += 2
                    continue
            # Check for the \xAB case, where A and B are
            # valid hexadecimal characters, in the ranges
            # (97 -> 102) for (a -> b) and (48 -> 57) for
            # (0 -> 9)
            if ptr + 3 < string_length:
                if ascii[ptr + 1] == 120: # Check for the singe 'x'
                    hex_1 = ascii[ptr + 2]
                    hex_2 = ascii[ptr + 3]
                    # Verify both as in range
                    if (
                        ((hex_1 >= 97 and hex_1 <= 102) or (hex_1 >= 48 and hex_1 <= 57) ) and
                        ((hex_2 >= 97 and hex_2 <= 102) or (hex_2 >= 48 and hex_2 <= 57) ) ):
                        byte_count += 1
                        ptr += 4
                        continue

        # Default case: add this character's byte and iterate
        byte_count += 1
        ptr += 1

    sum += len(line) - byte_count

print("Sum: %d" % sum)