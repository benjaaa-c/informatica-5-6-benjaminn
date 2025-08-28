greeting = input("Type a greeting: ")

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    greeting = money + 20
    print(f"${greeting}")
else:
    greeting = money + 100
    print(f"Your total is ${money}")

