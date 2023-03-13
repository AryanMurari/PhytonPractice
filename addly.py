a = input("Enter string: ")

if len(a) > 3 and a.endswith("ing"):
    new_str = a + "ly"
    print(new_str)
else:
    print(a)
