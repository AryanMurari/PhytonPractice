num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 3 == 0:
        print(num, "is divisible by both 2 and 3")
    else:
        print(num, "is divisible by 2 but not by 3")
elif num % 3 == 0:
    print(num, "is divisible by 3 but not by 2")
else:
    print(num, "is not divisible by either 2 or 3")
