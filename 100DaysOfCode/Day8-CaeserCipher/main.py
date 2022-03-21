from chars import alphabet
from art import logo


def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to execute the program again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Thanks for using Caesar Cipher")
