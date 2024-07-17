checker = 0
while True:
    text = input("File name: ").strip().lower()
    for c in text:
        if c == ".":
            checker += 1
    if checker == 1:
        x, y = text.split(".")
        if y == "jpg":
            print("image/jpeg")
        elif y == "jpeg" or y == "gif" or y == "png":
            print("image/" + y)
        elif y == "pdf" or y == "zip":
            print("application/" + y)
        elif y == "txt":
            print("text/plain")
        else:
            print("application/octet-stream")
        break
    elif checker == 2:
        print("application/pdf")
        break
    else:
        print("application/octet-stream")
        break

