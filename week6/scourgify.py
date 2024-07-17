import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        convert(sys.argv[1], sys.argv[2])

def convert(first, last):
    try:
        with open(first) as firstFile:
            reader = csv.DictReader(firstFile)
            with open(last, "w") as lastFile:
                writer = csv.DictWriter(lastFile, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()

