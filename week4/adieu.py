import inflect
import sys
names = []
p = inflect.engine()

while True:
    try:
        text = input("Name: ")
        names.append(text)
    except EOFError:
        break

myList = p.join(names)
print(f"Adieu, adieu, to {myList}")



