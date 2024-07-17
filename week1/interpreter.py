text = input("Expression: ")

x, y, z = text.split(" ")

x = float(x)
z = float(z)

if y == "+":
    print(round((x + z), 2))
elif y == "-":
    print(round((x - z), 2))
elif y == "*":
    print(round((x * z), 2))
else:
    print(round((x / z), 2))
