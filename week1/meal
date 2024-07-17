def main():
    time = input("What time is it? ")
    newTime = convert(time)
    if newTime >= 7 and newTime <= 8:
        print("breakfast time")
    elif newTime >= 12 and newTime <= 13:
        print("lunch time")
    elif newTime >= 18 and newTime <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    returnValue = round((int(hours) + ((int(minutes) * 1.66667) / 100)), 2)
    return returnValue

if __name__ == "__main__":
    main()
