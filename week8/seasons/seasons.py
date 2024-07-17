from datetime import date
import re
import inflect
import sys
p = inflect.engine()

def main():
    Date = input("Date of Birth: ")
    new = convert(Date)
    print(new)

def convert(Date):
    if matches := re.search(r"^([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])$", Date):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        past = date(year, month, day)
        current = date.today()
        value = current - past
        d = value.days * 24 * 60
        return f"{(p.number_to_words(d, andword="")).capitalize()} minutes"
    else:
        sys.exit("invalid")

if __name__ == "__main__":
    main()
