import sys

def abort(msg: str, code: int = 1) -> None:
    print(msg)
    sys.exit(code)

# 1. Check for correct usage
if len(sys.argv) != 2:
    abort("Usage: python color_select.py <colors.txt>")

# 2. Load colors from file
filename = sys.argv[1]
try:
    colors = [line.strip() for line in open(filename, encoding="utf-8") if line.strip()]
except FileNotFoundError:
    abort(f"Error: File '{filename}' not found.")

if not colors:
    abort("Error: No colors found in file.")

# 3. Show available options with numbers
print("Available colors:")
for idx, color in enumerate(colors, start=1):
    print(f"{idx}. {color}")

# 4. Get and validate user input (numeric)
choice = input("Enter the number of your color choice: ").strip()

if not choice.isdigit():
    abort(f"Error: '{choice}' is not a valid positive integer.")

index = int(choice) - 1  # convert to 0-based

if 0 <= index < len(colors):
    print(f"You selected: {colors[index]}")
else:
    abort(f"Error: {choice} is out of range (1-{len(colors)}).")
