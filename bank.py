x = input("Greeting: ").lower().lstrip(' ')

if x.startswith("hello"):
    print("$0")
elif x.startswith('h'):
    print("$20")
else:
    print("$100")


