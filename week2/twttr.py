text = input("Input: ")
print("Output: ", end = "")
list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for c in text:
    if c in list:
        print(end = "")
    else:
        print(c, end = "")
print()
