import random

# Computer thinks of a number between 1 and 20
target = random.randint(1, 20)

# Keep asking for guesses until correct or user quits
while True:
    user_input = input("Guess a number between 1 and 20 (or 'x' to quit): ")
    
    # Check if user wants to quit
    if user_input.lower() == 'x':
        print("Game over!")
        break
    
    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a valid integer or 'x' to quit.")
        continue
    
    if guess < target:
        print("Your guess is too low.")
    elif guess > target:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number!")
        break 