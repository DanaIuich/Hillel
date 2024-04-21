
# Output the maximum number of 3 user-entered numbers.
# DO NOT use built-in functions. Use only flow control instructions (ifs, loops)

# Solution 1
user_input1 = int(input("Enter the first number: "))
user_input2 = int(input("Enter the second number: "))
user_input3 = int(input("Enter the third number: "))
max_number = user_input1
if user_input2 > max_number:
    max_number = user_input2
if user_input3 > max_number:
    max_number = user_input3
print(f"The maximum number is {max_number}")


#Solution 2
max_number = 0
for i in range(3):
    user_input = int(input("Enter the number: "))
    if user_input > max_number:
        max_number = user_input
print(max_number)



