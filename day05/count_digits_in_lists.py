# List of numbers to analyze
numbers = [1203, 1256, 312456, 98]

# Create a list to store the count of each digit
digit_count = [0] * 10  # Creates a list of 10 zeros

# Loop through each number in the list
for number in numbers:
    number_str = str(number)
    
    # Loop through each digit in the number
    for digit in number_str:
        digit_count[int(digit)] += 1

for digit in range(10):
    print(f"{digit}  {digit_count[digit]}") 