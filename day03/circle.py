import math
import sys

# Circle's radius
radius = float(sys.argv[1])

# Calculate the area
area = math.pi * radius**2

# Calculate the circumference
circumference = 2 * math.pi * radius

# Print the results
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
