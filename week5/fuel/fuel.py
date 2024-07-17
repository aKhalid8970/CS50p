def main():
    value = input("Fraction: ")
    x = convert(value)
    y = gauge(x)
    print(y)


def convert(arg):
    while True:
        try:
            z, y = arg.split("/")
        except:
            pass
        else:
            if y == "0":
                raise ZeroDivisionError
            elif int(z) > int(y):
                raise ValueError
            else:
                x = int(z) / int(y) * 100
                return str(x)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage == 99 or percentage == 100:
        return "F"
    else:
        return f"{round(percentage)}"


if __name__ == "__main__":
    main()
