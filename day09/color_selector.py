import sys
from color_utils import load_colors, get_color_mapping, validate_color_choice

def main():
    # Check if user gave the right number of arguments
    if len(sys.argv) < 2:
        print("Error: You need to give a file name!")
        print("How to use: python color_selector.py colors.txt")
        sys.exit(1)
    
    if len(sys.argv) > 2:
        print("Error: You gave too many arguments!")
        print("How to use: python color_selector.py colors.txt")
        sys.exit(1)

    # Get the filename from command line
    filename = sys.argv[1]
    
    # Try to load the colors
    colors = load_colors(filename)
    
    # If no colors were loaded, exit
    if len(colors) == 0:
        print("Error: Could not load any colors from the file.")
        sys.exit(1)
    
    # Show all the colors to the user
    print("Here are the colors you can choose from:")
    for color in colors:
        print("- " + color)
    
    # Ask user for their choice
    print("\nWhat color do you want?")
    choice = input("Type your color here: ")
    
    # Make the color mapping
    color_mapping = get_color_mapping(colors)
    
    # Check if the choice is valid
    is_valid, selected_color = validate_color_choice(choice, color_mapping)
    
    # Tell user if their choice was good or bad
    if is_valid == True:
        print("Good choice! You picked: " + selected_color)
    else:
        print("Sorry, that's not a valid color!")
        print("You typed: " + choice)
        print("Please try again with one of the colors from the list above.")

# Run the program
if __name__ == "__main__":
    main() 