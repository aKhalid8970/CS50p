list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ")
        for i in date:
            if i.isalnum() == False:
                x = i
        if date.find("/") != -1 or date.find("-") != -1:
            month, day, year = date.split(x)
            if month in list:
                month = list.index(month) + 1
                print(year + "-" + str(month).zfill(2) + "-" + day.zfill(2))
                exit()
            else:
                continue
        else:
            month, day, year = date.split(" ")
            if month in list:
                month = list.index(month) + 1
                day = day.replace(",", "")
                print(year + "-" + str(month).zfill(2) + "-" + day.zfill(2))
                exit()
            else:
                continue

main()


