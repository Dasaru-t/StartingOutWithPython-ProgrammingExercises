# 3. Budget Analysis

# Get the budget
budget = float(input('Enter the amount you budgeted for a month. :'))

total = 0.0
another = 'y' # Variable to control the loop.
count = 0

while another == 'y' or another == 'Y':
  print("Enter your expense",count + 1)
  expense = float(input(":"))
  total += expense 
  print('Total expenses: ',total)
  count += 1

  # Do this again?
  another = input("\nDo you want to enter another expense(enter y for yes & n for no): ")

if total < budget:
  status = "You are under budget"

elif total > budget:
  status = "You are over budget"

else:
  status = "You're budget and expenses are equal"

print(status) 
print("Your budget for this month: $",budget)
print("Your total expenses: $",total)
