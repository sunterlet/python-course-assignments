#!/usr/bin/env python3
import sys

# Check for correct usage
if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <colors_file>")
    sys.exit(1)

# Load colors
filename = sys.argv[1]
try:
    colors = [line.strip() for line in open(filename, encoding='utf-8') if line.strip()]
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

if not colors:
    print("Error: No colors found in file.")
    sys.exit(1)

# Show available options
print("Available colors:", ", ".join(colors))

# Get and validate user input (case-insensitive)
choice = input("Enter a color: ").strip().lower()
mapping = {c.lower(): c for c in colors}

if choice in mapping:
    print(f"You selected: {mapping[choice]}")
else:
    print(f"Error: '{choice}' is not a valid color.")
