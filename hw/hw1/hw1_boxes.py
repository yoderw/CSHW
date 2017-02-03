"""
Width? 3
Number? 4

+---+ +---+ +---+ +---+
|   | |   | |   | |   |
+---+ +---+ +---+ +---+
"""

width = int(input("Width? "))
number = int(input("Number? "))

print()

print(("+" + ("-" * width) + "+" + " ") * (number - 1) + ("+" + ("-" * width) + "+"))
print(("|" + (" " * width) + "|" + " ") * (number - 1) + ("|" + (" " * width) + "|"))
print(("+" + ("-" * width) + "+" + " ") * (number - 1) + ("+" + ("-" * width) + "+"))