def main():
    message = input("type a message: ").lower()
    encode_message(message)


def encode_message(text):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    cipher = "zywvutsrqponmlkjihgfedcba"
    new_message = ""
    i = 0

    while i < len(text):
        char = text[i]

        if char in alphabet:
            cipher_index = alphabet.find(char)
            new_message += cipher[cipher_index]
        else:
            new_message += char
        i += 1
        print("Enconded message :" + new_message)

main()