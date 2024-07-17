list = {}

def main():
    while True:
        try:
            convert()
        except EOFError:
            sorted_keys = sorted(list.keys())
            for i in sorted_keys:
                print(list[i], i)
            exit()

def convert():
    while True:
        counter = 1
        try:
            item = input().upper()
            if item in list:
                list[item] += 1
            else:
                list[item] = counter
        except KeyError:
            pass

main()
