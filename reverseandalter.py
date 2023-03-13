string = "Hello Python Program!!"

reverse_string = ""
i = 0
while True:
    try:
        char = string[-(i + 1)]
        reverse_string += char
        i += 1
    except IndexError:
        break

i = 0
while True:
    try:
        char = reverse_string[i]
        if i % 2 == 0:
            print(char, end="")
        i += 1
    except IndexError:
        break
