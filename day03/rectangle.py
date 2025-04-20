import sys

# Rectangle's height and width
height = float(sys.argv[1])
width =  float(sys.argv[2])

# Calculate the area
area = height * width

# Calculate the perimeter
perimeter = 2 * (height + width)

# Print the results
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
