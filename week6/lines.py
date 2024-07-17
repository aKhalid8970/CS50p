import sys
counter = 0
checker = 2
lis = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
else:
    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        for line in file:
                if not line.lstrip().startswith("#") and line.lstrip() != "":
                    counter += 1

        file.close()
        print(counter)
        sys.exit(0)
