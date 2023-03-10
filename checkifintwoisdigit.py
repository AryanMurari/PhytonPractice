user_input = input("Enter a string: ")

# check if the string contains only digits
is_integer = True
for char in user_input:
    if char < '0' or char > '9':
        is_integer = False
        break

if is_integer:
    print("The string is an integer.")
else:
    print("The string is not an integer.")
