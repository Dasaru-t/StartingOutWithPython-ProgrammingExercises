# 4. Distance Traveled

#asks the user for the speed of a vehicle (in miles per hour)
speed = int(input("Enter the speed of a vehicle (in miles per hour): "))

#asks the user for the number of hours it has traveled.
time = int(input("Enter the number of hours traveled: "))

print("\nHour\tDistance Traveled")
print("--"*12)

for t in range(1,time + 1):
  distance = speed * t  # Calculate the distance
  print(t ,"\t\t",distance)