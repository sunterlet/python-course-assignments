import random

# Computer thinks of a number between 1 and 20
target = random.randint(1, 20)

# Keep asking for guesses until correct or user quits
while True:
    user_input = input("Guess a number between 1 and 20 (or 'x' to quit, 's' to see the number): ")
    
    # Check if user wants to quit
    if user_input.lower() == 'x':
        print("Game over!")
        break
    
    # Check if user wants to cheat
    if user_input.lower() == 's':
        print("The number is", target)
        continue
    
    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a valid integer, 'x' to quit, or 's' to see the number.")
        continue
    
    if guess < target:
        print("Your guess is too low.")
    elif guess > target:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number!")
        break 