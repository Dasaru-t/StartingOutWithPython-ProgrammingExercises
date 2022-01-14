# 7. Pennies for Pay

# ask the user for the number of days.
days = int(input("Enter the number of days: "))

# Initialize an accumulator variable.
total = 0.0

# print headings
print("\nDay\tSalary")
print("-"*14)

for d in range(days):
  salary = 2**d
  dollar = salary / 100
  total += dollar

  print(d+1,"\t","$",format(dollar,",.2f"))

# Display total
print("\nTotal pay $",format(total,",.2f"))