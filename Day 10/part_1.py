def look_and_say(input: str) -> str:
    output = ""

    # Index used as a string pointer
    ptr = 0
    string_length = len(input)

    while ptr < string_length:
        char = input[ptr]

        # Count repeats of this character
        repeats = 0
        while ptr + repeats + 1 < string_length:
            if input[ptr + repeats + 1] == char:
                repeats += 1
            else:
                break
        
        output += "%d%s" % (int(1 + repeats), char)
        ptr += 1 + repeats
    return output

seed = "3113322113"
for _ in range(40):
    seed = look_and_say(seed)

print(len(seed))