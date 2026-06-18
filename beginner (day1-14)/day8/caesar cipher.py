alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

def caesar(text, shift_amount, direction):
    result = ""

    if direction == "decode":
        shift_amount *= -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            result += alphabet[new_position]
        else:
            result += letter

    print(f"Here's the {direction}d result: {result}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(text, shift, direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")