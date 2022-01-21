#3.  How Much Insurance?

#Global costant
INSURANCE_PERCENTAGE= 0.8

def main():
  #Get the replacement cost
  cost = get_cost()

  #Calculate the minimum amount
  minimum = minimum_amount(cost)

  #Display the results
  print("Your insurance amount is : $",format(minimum,",.2f"))

# The get_cost function prompts the
# user to enter cost of a building and it
# returns that value.
def get_cost():
  cost = float(input("Enter the replacement cost of a building: "))
  return cost

# The minimum_amount function accepts an cost
# as an argument and returns the minimum_cost
# specified by INSURANCE_PERCENTAGE.
def minimum_amount(cost):
  return cost * INSURANCE_PERCENTAGE

# Call the main function.
main()