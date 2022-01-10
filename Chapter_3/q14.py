# 14. Body Mass Index

#ask the user to enter his or her weight
weight = float(input("Enter your weight(in pounds): "))

#ask the user to enter his or her height
height = float(input("Enter your height(in inches): "))

# calculate BMI
bmi = weight * 703.0 / (height**2)

if bmi < 18.5:
  status = "Underweight"

elif bmi <= 25:
  status = "Optimal Weight"

else:
  status = "Overweight"

print("\nYou'r BMI is :",format(bmi,'.2f'))
print("You are",status,"person")