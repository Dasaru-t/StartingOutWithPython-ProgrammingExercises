from caroopin10 import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("BMW","M5",2020,"Red")
car_3 = Car("Toyota","Supra",2008,"Black")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

print(car_3.make)
print(car_3.model)
print(car_3.year)
print(car_3.color)

car_3.drive()
car_3.stop()