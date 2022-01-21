#4. Automobile Costs

def main():
  #Get the monthly costs
  loan, insurance, gas, oil, tires, maintenance = get_cost()

  #Calculate the total cost
  total, annual = total_cost(loan, insurance, gas, oil, tires, maintenance)

  #Display the results
  print("\nYour total monthly cost is: $",total)
  print("Your total annual cost is: $",annual)


# The get_cost function prompts the
# user to enter cost of a building and it
# returns those values.
def get_cost():
  print("Enter monthly expenses incurred from operating your automobile\n")
  loan = float(input("Enter the monthly loan payment cost: "))
  insurance = float(input("Enter the monthly insuarance cost: "))
  gas = float(input("Enter the monthly gas cost: "))
  oil = float(input("Enter the monthly oil cost: "))
  tires = float(input("Enter the monthly tires cost: "))
  maintenance = float(input("Enter the monthly maintenance cost: "))
  #return values
  return loan, insurance, gas, oil, tires, maintenance

# Calculate the total cost & total annual cost
# The total_cost function accepts six
# arguments and returns the total and annual
def total_cost(loan, insurance, gas, oil, tires, maintenance):
  total = loan + insurance + gas + oil + tires + maintenance
  annual = total * 12
  #return values
  return total, annual

# Call the main function.
main()