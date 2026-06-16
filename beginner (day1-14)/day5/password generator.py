import random

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("Welcome to the PyPassword Generator!")

lets = int(input("How many letters would you like in your password? "))
symb = int(input("How many symbols would you like? "))
numb = int(input("How many numbers would you like? "))

print("Easy level")

password = ""

for _ in range(lets):
    password += random.choice(letters)

for _ in range(symb):
    password += random.choice(symbols)

for _ in range(numb):
    password += random.choice(numbers)

print(password)

print("HARD LEVEL")

password_list = []

for _ in range(lets):
    password_list.append(random.choice(letters))

for _ in range(symb):
    password_list.append(random.choice(symbols))

for _ in range(numb):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")