from header import header

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    caesar_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():
            if direction == "decode":
                position = alphabet.index(char) + 26
            else:
                position = alphabet.index(char)
            new_position = position + shift_amount
            caesar_text += alphabet[new_position]
        else:
            caesar_text += char

    print(f"Here's the {cipher_direction}d result: {caesar_text}")


print(header)

in_program = True

while in_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    continue_program = input(
        "\nDo you want to restart the Caesar Cipher program?\nType 'yes' if you want to go again. Otherwise type 'no'. -> "
    )

    if continue_program == "no":
        in_program = False
        print("Goodbye!")
