import sys

# Check if sequence is provided as command line argument
if len(sys.argv) != 2:
    print("Please provide a sequence as command line argument")
    sys.exit(1)

# Get the sequence from command line argument
sequence = sys.argv[1]

# Split the sequence by 'X' and filter out empty strings
sequences = sequence.split('X')
new_sequences = []
for seq in sequences:
    if seq:  
        new_sequences.append(seq) 

# Sort sequences by length (longest first)
new_sequences.sort(key=len, reverse=True)

print(new_sequences) 
