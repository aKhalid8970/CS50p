import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        counter = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                counter += 1
                if counter == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
            else:
                if answer != x + y:
                    print("EEE")
                    counter += 1
                    if counter == 3:
                        print(f"{x} + {y} = {x + y}")
                        break
                else:
                    score += 1
                    break
        print(f"Score: {score}")


def get_level():
    while True:
        try:
            digits = int(input("Level: "))
        except ValueError:
            pass
        else:
            if digits == 1 or digits == 2 or digits ==3:
                return digits


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()
