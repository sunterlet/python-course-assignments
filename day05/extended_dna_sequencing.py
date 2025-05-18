# Ask for input
print("Please type in a sequence:")
sequence = input().strip()

# Create a list to store valid sequences
valid_sequences = []
current_sequence = ""

# Go through each character in the sequence
for char in sequence:
    # If the character is a valid nucleotide (A, C, T, G)
    if char in "ACTG":
        current_sequence += char
    else:
        # If we have a valid sequence, add it to our list
        if current_sequence:
            valid_sequences.append(current_sequence)
            current_sequence = ""

# Sort sequences by length (longest first)
valid_sequences.sort(key=len, reverse=True)

print(valid_sequences) 