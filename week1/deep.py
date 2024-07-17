while True:
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if x == "42" or x == "forty two" or x == "forty-two":
        print("Yes")
        break
    else:
        print("No")
        break
