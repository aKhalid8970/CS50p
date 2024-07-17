import sys
import csv
from tabulate import tabulate
dic = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith("csv") != True:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1], newline='') as file:
            reader = csv.reader(file)
            for i in reader:
                dic.append(i)
        print(tabulate(dic, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exit")

