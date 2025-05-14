import random

# Computer thinks of a number between 1 and 20
target = random.randint(1, 20)
debug_mode = False

# Keep asking for guesses until correct or user quits
while True:
    # Show debug info if debug mode is on
    if debug_mode:
        print("Debug: The number is", target)
    
    user_input = input("Guess a number between 1 and 20 (or 'x' to quit, 's' to see the number, 'd' to toggle debug): ")
    
    # Check if user wants to quit
    if user_input.lower() == 'x':
        print("Game over!")
        break
    
    # Check if user wants to cheat
    if user_input.lower() == 's':
        print("The number is", target)
        continue
    
    # Toggle debug mode
    if user_input.lower() == 'd':
        debug_mode = not debug_mode
        print("Debug mode is", "on" if debug_mode else "off")
        continue
    
    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a valid integer, 'x' to quit, 's' to see the number, or 'd' to toggle debug.")
        continue
    
    if guess < target:
        print("Your guess is too low.")
    elif guess > target:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number!")
        break 