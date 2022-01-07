# 5. Mass and Weight

#asks the user to enter an object’s mass
mass = float(input("Enter an object’s mass: "))

#calculating the weight
weight = mass * 9.8

if weight > 500:
  print("Object weighs is",format(weight,'.2f'),"newtons. it's more than 500 newtons, it's too heavy.")
elif weight < 100:
  print("Object weighs is",format(weight,'.2f'),"newtons. it's less than 100 newtons, it's too light.")
else:
  print("Object weighs is",format(weight,'.2f'),"newtons.")

  