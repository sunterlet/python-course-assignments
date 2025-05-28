import sys, codecs

# Ensure a filename is provided
if len(sys.argv) != 2:
    print("Please enter a valid txt file")
    sys.exit(1)

fn = sys.argv[1]

# Read, transform, and overwrite in three simple steps
with open(fn, 'r', encoding='utf-8') as f:
    data = f.read()

data = codecs.encode(data, 'rot_13')

with open(fn, 'w', encoding='utf-8') as f:
    f.write(data)

print(f"ROT13 applied to '{fn}'")
