starting = 50
while True:
    print(f"Amount Due: {starting}")
    x = int(input("Insert Coin: "))
    if x != 25 and x != 10 and x != 5:
        print(f"Amount Due: {starting}")
        continue
    elif x < starting:
        starting -= x
        continue
    elif x == starting:
        print("Change Owed: 0")
        break
    else:
        z = x - starting
        print(f"Change Owed: {z}")
        break
