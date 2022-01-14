from art import logo

def play(index=None):
    print("\n")
    print(logo)
    be_continue = True
    while be_continue:
        direction = input ("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26

        caesar(start_text=text, cipher_direction=direction, shift_amount=shift)

        should_continue = input ("Do you wanna try again? Type 'Y' or 'N'\n").lower()
        if should_continue == "n":
            be_continue = False
            print("\nEnd program\n")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
            else:
                new_position = position - shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


if __name__ == "__main__":
    play()