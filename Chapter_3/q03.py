# 3. Age Classifier

#asks the user to enter a person’s age
age = float(input("Enter a person's age: "))

if age <= 1:
  person = "infant" 
elif age > 1 and age < 13:
  person = "child"
elif age >= 13 and age < 20:
  person = "teenager"
else:
  person = "adult"

print("This person is",age,"years old",person)

