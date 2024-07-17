text = input("camelCase: ")
print("snake_case: ", end = "")

for c in text:
    if c.isupper() == True:
        print("_" + c.lower(), end = "")
    else:
        print(c, end = "")
print()
