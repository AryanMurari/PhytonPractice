'''Take a string from user if the string is grater than 3 and ends with 'ing' add ly to it and print result
else print original string'''

a = input("Enter string: ")

if len(a) > 3 and a.endswith("ing"):
    new_str = a + "ly"
    print(new_str)
else:
    print(a)
