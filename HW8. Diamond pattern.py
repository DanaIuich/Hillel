# The user enters the minimum and maximum width of the diamond pattern.
# Print a "diamond" with given dimensions composed of '*' symbols.
# If the entered minimum width is greater than the maximum width, print a warning and terminate the program.
# If the difference between the maximum and minimum widths is not a multiple of 2, print a warning and terminate the program.
# There are NO spaces at the end of lines.
# DO NOT use methods of string type

min_width = int(input("Enter minimal width: "))
max_width = int(input("Enter maximal width: "))
symbol = '*'

if min_width > max_width:
    print("Warning! Minimal width is more than maximal width")
elif (max_width - min_width) % 2 != 0:
    print("Warning! The difference between the maximum and minimum widths is not a multiple of 2")
else:
    for i in range(min_width, max_width+1, 2):
        space_outer = ' ' * ((max_width - i) // 2)
        if i == min_width:
            print(space_outer+symbol*i)
        else:
            space_inner = ' ' * (i - 2)
            print(space_outer+symbol+space_inner+symbol)
    for i in range(max_width-2, min_width-1,-2):
        space_outer = ' ' * ((max_width - i) // 2)
        if i == min_width:
            print(space_outer+symbol*i)
        else:
            space_inner = ' ' * (i - 2)
            print(space_outer+symbol+space_inner+symbol)





