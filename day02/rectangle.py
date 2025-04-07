# Rectangle's height and width
height_str = input("Enter the rectangle's height: ")
width_str = input("Enter the rectangle's width: ")
height = float(height_str)
width = float(width_str)

# Calculate the area
area = height * width

# Calculate the perimeter
perimeter = 2 * (height + width)

# Print the results
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
