def main():
    password = input("Set password: ")
    input("Press enter to log in.")
    check_password(password)

def check_password():
    guess = input("enter password: ")
    if B == guess:
        print("Correct password")

main()