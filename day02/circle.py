import math

# Circle's radius
radius_str = input("Enter the circle's radius: ")
radius = float(radius_str)

# Calculate the area
area = math.pi * radius**2

# Calculate the circumference
circumference = 2 * math.pi * radius

# Print the results
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
