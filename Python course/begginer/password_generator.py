#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?: " )) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))

pw_length = nr_letters + nr_numbers + nr_symbols
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""
tmp_lett, tmp_sym = nr_letters, nr_symbols
for i in range(pw_length):
    if tmp_lett > 0:
        easy_password += random.choice(letters)
        tmp_lett -= 1
    elif tmp_sym > 0:
        easy_password += random.choice(symbols)
        tmp_sym -= 1
    else:
        easy_password += random.choice(numbers)

print(f"\nEasy password: {easy_password}\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = []
tmp_lett, tmp_sym  = nr_letters, nr_symbols
for i in range(pw_length):
    if tmp_lett > 0:
        hard_password += random.choice(letters)
        tmp_lett -= 1
    elif tmp_sym > 0:
        hard_password += random.choice(symbols)
        tmp_sym -= 1
    else:
        hard_password += random.choice(numbers)

random.shuffle(hard_password)
password = ""
for char in hard_password:
    password += char
print(f"Hard password: {password}\n")