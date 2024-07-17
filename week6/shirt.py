from PIL import Image, ImageOps
import sys
import os.path

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        _, ext1 = os.path.splitext(sys.argv[1])
        _, ext2 = os.path.splitext(sys.argv[2])
        print(ext1)
        if ext1 != ext2:
            sys.exit("Input and output have different extensions")
        elif ext1 != ".jpg" and ext1 != ".jpeg" and ext1 != ".png":
            sys.exit("Invalid extension given")
        else:
            try:
                edit(sys.argv[1], sys.argv[2])
            except FileNotFoundError:
                sys.exit("Input does not exit")

def edit(first, second):
    shirt = Image.open("shirt.png")
    original = Image.open(first)
    dimensions = shirt.size
    cropped = ImageOps.fit(original, dimensions)
    cropped.paste(shirt, shirt)
    cropped.save(second)

if __name__ == "__main__":
    main()
