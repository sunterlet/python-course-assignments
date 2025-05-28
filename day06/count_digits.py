import sys

# Ensure a filename is provided
if len(sys.argv) != 2:
    print("Please enter a valid txt file")
    sys.exit(1)

# Read entire file
fn = sys.argv[1]
text = open(fn, 'r', encoding='utf-8').read()

# Count each digit 
counts = {str(d): text.count(str(d)) for d in range(10)}

# Write results
with open('report.txt', 'w', encoding='utf-8') as out:
    for digit in sorted(counts):
        out.write(f"{digit} {counts[digit]}\n")

print("Report saved to report.txt")
