text = input("Greeting: ").lower().strip()

if text.startswith("hello"):
    print("$0")
elif text.startswith("h") and not text.startswith("hello"):
    print("$20")
else:
    print("$100")
