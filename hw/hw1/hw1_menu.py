"""
Restaurant name? Bobby's
First entree? Pasta verde    
First entree price? 15
Second entree? Filet mignon w/ lobster and caviar
Second entree price? 107
Third entree? Hamburger with fries
Third entree price? 9

1234567890123456789012345678901234567890

Bobby's Entrees
---------------
Pasta verde.........................$ 15
Filet mignon w/ lobster and caviar..$107
Hamburger with fries................$  9
"""

restaurant_name = str(input("Restaurant name? "))
first_name = str(input("First entree? "))
first_price = str(input("First entree price? "))
second_name = str(input("Second entree? "))
second_price = str(input("Second entree price? "))
third_name = str(input("Third entree? "))
third_price = str(input("Third entree price? "))

line1 = "{} Entrees".format(restaurant_name)
line2 = "-" * len(line1)
line3 = first_name + ("." * (36 - len(first_name))) + "$" + (" " * (3 - len(first_price))) + first_price
line4 = second_name + ("." * (36 - len(second_name))) + "$" + (" " * (3 - len(second_price))) + second_price
line5 = third_name + ("." * (36 - len(third_name))) + "$" + (" " * (3 - len(third_price))) + third_price

print()
print("1234567890123456789012345678901234567890")
print()

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)