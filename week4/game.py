import random
import sys
n = 0
x = 0

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            n = random.randint(1, n)
            break

while True:
    try:
        x = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if x > n:
            print("Too large!")
        elif x < n:
            print("Too small!")
        else:
            print("Just right!")
            sys.exit(0)
