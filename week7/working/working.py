import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^([1-9]|(?:1[0-2]))(:[0-5][0-9])? (am|pm) to ([1-9]|(?:1[0-2]))(:[0-5][0-9])? (am|pm)", s.lower(), re.IGNORECASE):
        default2 = matches.group(2) or ":00"
        default5 = matches.group(5) or ":00"
        hour = [0, 0, 0, 0, 0]
        hour[1] = (matches.group(1))
        hour[4] = (matches.group(4))
        if matches.group(2) != None and int(matches.group(2).strip(":")) > 59:
            raise ValueError
        if matches.group(5) != None and int(matches.group(5).strip(":")) > 59:
            raise ValueError
        if matches.group(3) == "pm":
            hour1 = int(hour[1]) + 12
        if matches.group(6) == "pm":
            hour3 = int(hour[3]) + 12
        for i in [1, 4]:
            if matches.group(i) == "12":
                if matches.group(i + 2) == "pm":
                    hour[i] = 12
                else:
                    hour[i] = 0
        if matches.group(2) == None and matches.group(5) == None:
            return f"{str(hour[1]).zfill(2)}{default2} to {str(hour[3]).zfill(2)}{default5}"
        elif matches.group(2) != None and matches.group(5) == None:
            return f"{str(hour[1]).zfill(2)}{matches.group(2)} to {str(hour[3]).zfill(2)}{default5}"
        elif matches.group(2) == None and matches.group(5) != None:
            return f"{str(hour[1]).zfill(2)}{default2} to {str(hour[3]).zfill(2)}{matches.group(5)}"
        else:
            return f"{str(hour[1]).zfill(2)}{matches.group(2)} to {str(hour[3]).zfill(2)}{matches.group(5)}"
    else:
        raise ValueError

if __name__ == "__main__":
        main()
