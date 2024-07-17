def main():
    x = convert("Fraction: ")
    if x <= 0.01:
        print("E")
    elif x == 0.99 or x == 1:
        print("F")
    elif x > 1:
        main()
    else:
        print(f"{round(x * 100)}%")

def convert(prompt):
    while True:
        try:
            x = input(prompt)
            z, y = x.split("/")
            return int(z) / int(y)
        except:
            pass

main()
