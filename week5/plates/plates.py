def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    counter = 0
    #if len(s) < 2 or len(s) > 6:
        #return False
    #else:


    for x in s:
        if x == "0" and counter == 0:
            return False
        if x.isnumeric() == True:
            counter += 1
        elif x.isalpha() == True and counter > 0:
            return False
        elif x.isalnum() == False:
            return False
    if s[0].isnumeric() == True:
            return True
    return True

if __name__ == "__main__":
    main()
