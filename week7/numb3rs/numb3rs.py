import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"^([0-2]?\d\d?)\.([0-2]?\d\d?)\.([0-2]?\d\d?)\.([0-2]?\d\d?)$", ip):
        for i in range(1, len(matches.groups())):
            if int(matches.group(i)) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
