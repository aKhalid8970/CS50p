def main():
    text = input("Greeting: ").lower().strip()
    money = value(text)
    print(f"${money}")


def value(greeting):
    if greeting.startswith("hello"):
        return 100
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()
