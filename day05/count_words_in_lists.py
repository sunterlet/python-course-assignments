# List of celestial objects
celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

# Create a dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in celestial_objects:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word:} {count}")