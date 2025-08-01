import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
password_list = []
password = ' '
print("Welcome to password generator.")
no_letters = int(input("Number of letters you want in your password : "))
no_numbers = int(input("Number of numbers you want in your password : "))
no_symbols = int(input("Number of symbols you want in your password : "))
for letter in range(1, no_letters+1):
   char = random.choice(letters)
   password_list += char
for number in range(1, no_numbers+1):
   int = random.choice(numbers)
   password_list += int
for special in range(1, no_symbols+1):
   sym = random.choice(special_symbols)
   password_list += sym
random.shuffle(password_list)
for i in password_list:
   password += i
print(f"Password is : {password}")



