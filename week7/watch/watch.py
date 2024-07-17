import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r"^<iframe.+(https?://(?:www.)?)youtube.com/embed(/\w{11})", s, re.IGNORECASE):
        return "https://youtu.be" + matches.group(2)
    else:
        return "None"

if __name__ == "__main__":
    main()
