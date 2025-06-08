import sys

# Check for correct usage
if len(sys.argv) != 2:
    print("Input a valid text file")
    sys.exit(1)

filename = sys.argv[1]
counts = {}

# Read the file and count words
with open(filename, 'r') as f:
    for line in f:
        words = line.strip().split()
        for word in words:
            word = word.lower()
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

# Print results sorted by word
for word in sorted(counts):
    print(f"{word:<15} {counts[word]}")
