'''In 101111100100010001000011110101010 write code to print maximum number of acurance of 1s'''
a = input("Enter string: ")
#a = "1011111001000100010000111110101010"
count = 0
max_count = 0
for digit in a:
    if digit == '1':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print("The max number of 1s is:", max_count)
