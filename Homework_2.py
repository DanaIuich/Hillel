# 1. Create list of 3 cats/dogs names
#
# Output elements using coma and space:

animal_name = ['Murzik', 'Barsik', 'Pantera']
#Solution 1
print(animal_name[0]+',', animal_name[1]+',', animal_name[2])
#Solution 2
print(f"{animal_name[0]}, {animal_name[1]}, {animal_name[2]}")
#If we need to output a list:
print(animal_name)

# 2. Create list of 3 countries names.
#
# Create dictionary of 3 key-value pairs.
#
# Key should be country name from the list and value should be string with its capital.
#
# Output each pair on separate lines. Separate key from value with colon and space:

country_list = ['Ukraine', 'Spain', 'Italy']
country_dict = {country_list[0]: 'Kyiv', country_list[1]: 'Madrid', country_list[2]: 'Rome'}
#Solution 1
print(country_list[0]+':', country_dict[country_list[0]])
print(country_list[1]+':', country_dict[country_list[1]])
print(country_list[2]+':', country_dict[country_list[2]])
#Solution 2
for key, value in country_dict.items():
    print(f"{key}: {value}")


# 3. Request two integer numbers from user.
#
# Output on one line expression with sum of numbers, and on another line - expression with product of numbers:
user_input1 = int(input("Enter a: "))
user_input2 = int(input("Enter b: "))
#Solution 1
print(user_input1 + user_input2)
print(user_input1 * user_input2)
#Solution 2
print(f'{user_input1} + {user_input2} = {user_input1 + user_input2}')
print(f'{user_input1} * {user_input2} = {user_input1 * user_input2}')

