# Make the increment and password
# check files using a list of 8
# integers in the range 0-25 representing
# the lowercase letters a -> b
def increment(input: [int]) -> [int]:
    # Loop from right, carrying a 1
    bytes = list(input)
    i = 7
    while i >= 0:
        bytes[i] += 1
        if bytes[i] < 26:
            # Check for the special cases where
            # the character is i, o, or l.
            # In these cases, any value with these
            # characters will not be valid as passwords,
            # so increment again (to j, p, or m) and set
            # any following digits to a (0)
            if bytes[i] == 8 or bytes[i] == 11 or bytes[i] == 14:
                bytes[i] += 1
                for j in range(i + 1, 8):
                    bytes[j] = 0
            break
        # Set this digit to 0 and iterate
        bytes[i] = 0
        i -= 1
    return bytes

# Take a string of lowercase letters and
# convert it to a list of integers in
# the range 0 -> 25
def string_to_bytes(input: str) -> [int]:
    bytes = list(input.encode("ascii"))
    for i in range(8):
        bytes[i] -= 97
    return bytes

def bytes_to_string(input: [int]) -> str:
    bytes = list(input)
    for i in range(8):
       bytes[i] += 97
    return "".join(map(chr, bytes))

def is_password(input: [int]) -> bool:
    #Verify there is an increasing sequence
    has_increasing_sequence = False
    for i in range(6):
        if input[i + 1] == input[i] + 1 and input[i + 2] == input[i] + 2:
            has_increasing_sequence = True
            break
    if not has_increasing_sequence:
        return False
    
    # See if any of the disallowed letters are present
    for i in range(8):
        if input[i] == 8 or input[i] == 11 or input[i] == 14:
            return False
        
    # Verify there are two sets of double letters.
    first_doubled_letter = -1
    ptr = 0
    while ptr < 7:
        if input[ptr] == input[ptr + 1]:
            if first_doubled_letter == -1:
                first_doubled_letter = input[ptr]
                ptr += 2
            else:
                return True
        else:
            ptr += 1


password = "cqjxxyzz"
bytes = increment(string_to_bytes(password))
while not is_password(bytes):
    bytes = increment(bytes)
print(bytes_to_string(bytes))