from validator_collection import checkers

def main():
    print(convert(input("What's your email address? ")))

def convert(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
