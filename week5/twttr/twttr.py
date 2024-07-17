def main():
    text = shorten(input("Input: "))
    print(f"Output: {text}")

def shorten(word):
    return word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")



if __name__ == "__main__":
    main()
