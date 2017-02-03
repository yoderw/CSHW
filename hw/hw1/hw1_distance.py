location_x = float(input("Location x-coordinate? "))
location_y = float(input("Location y-coordinate? "))
class_x = float(input("Classroom x-coordinate? "))
class_y = float(input("Classroom y-coordinate? "))

x = class_x - location_x
y = class_y - location_y

distance = ((x ** 2) + (y ** 2)) ** 0.5

print(distance)