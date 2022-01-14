# 8. Sum of Numbers

#asks the user to enter a series of positive numbers
num = int(input("Enter a positive number: "))

# Initialize an accumulator variable.
total = 0.0

while num >= 0:
  total += num
  num = int(input("Enter a positive number to continue or negative number to end: "))
  
# Display total sum
print("Total sum is:",total)

