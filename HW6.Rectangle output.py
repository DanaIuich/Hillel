# User enters height and width of rectangle (integer numbers), and any symbol.
# Output a rectangle made up of the entered character of a given size.
# There are NO spaces at the end of lines.

rect_height = int(input("Enter height of rectangular: "))
rect_width = int(input("Enter width of rectangular: "))
symbol = input("Enter symbol to build rectangular with: ")
for i in range(rect_height):
    rect = rect_width * symbol
    print(rect)


