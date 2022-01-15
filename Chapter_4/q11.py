# 11. Calculating the Factorial of a Number

# ask user to enter a nonnegative number
number = int(input("Enter a non negative integer: "))

while number <= 0:
  number = int(input("Error! enter a non negative integer: "))

# Initialize an accumulator variable.
factorial = 1

for num in range(1,number+1):
  factorial = factorial * num

print("\nFactorial of",number,"is",factorial)