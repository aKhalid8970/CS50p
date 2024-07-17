from pyfiglet import Figlet
import sys
import random

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit(1)

if sys.argv[1] != '-f':
    sys.exit(1)

figlet = Figlet()

fonts = figlet.getFonts()
text = input("Input: ")
print("Output: ")

if len(sys.argv) == 3:
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(text))

else:
    figlet.setFont(font = random.choice(fonts))
    print(figlet.renderText(text))


