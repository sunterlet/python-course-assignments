import random

# Computer thinks of a number between 1 and 20
target = random.randint(1, 20)

# User makes one guess
guess = int(input("Guess a number between 1 and 20: "))

# Guess check
if guess < target:
    print("Your guess is too low.")
elif guess > target:
    print("Your guess is too high.")
else:
    print("Congratulations! You guessed the number!")
