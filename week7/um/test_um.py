import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    lis = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(lis)

if __name__ == "__main__":
    main()
