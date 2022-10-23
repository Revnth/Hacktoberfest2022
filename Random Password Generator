import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("-                  #RANDOM PASSWORD GENERATOR#",end="\n\n")

pass_letters = int(input("How many letters would you like in your password?\n=> "))
pass_symbols = int(input(f"\nHow many symbols would you like?\n=> "))
pass_numbers = int(input(f"How many numbers would you like?\n=> "))

password_list = []

for char in range(1, pass_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, pass_symbols + 1):
    password_list.append(random.choice(numbers))

for char in range(1, pass_numbers + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char


# convert list to string
paswd = ''.join(password_list)
print(f"Your random password to use is: {paswd}")
