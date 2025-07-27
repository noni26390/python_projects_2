import random 

# ask user name
#  
Name = input("Enter you name: ")

# ask favourite colour 

Color = input("Enter you Favourite color: ")

# ask birth year

Birth_year = input("Enter you Birth year: ")

symbol_list = ['!', '@', '#', '$', '%', '&']

symbol = random.choice(symbol_list)

number = random.randint(10, 99)

password = Name[:2].capitalize() + Color[-2:].lower() + Birth_year[-2:] + symbol + str(number)

print(password)