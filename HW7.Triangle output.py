# Output a triangle of user-entered size.
# There are NO spaces at the end of lines.
# DO NOT use methods of string type.
user_input = int(input("Enter size of triangle: "))
symbol = '*'
for i in range(user_input+1):
    space = ' ' * (user_input - i)
    tri = symbol * i
    print(space+tri)







