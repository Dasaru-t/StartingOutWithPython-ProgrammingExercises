# 2. Sales Tax Program Refactoring

#Global costant
STATE_TAX_PERCENTAGE = 0.05
COUNTRY_TAX_PERCENTAGE = 0.025

# The main function.
def main():
  #Get the amount of a purchase
  amount = get_amount()
  # Calculate the state tax
  state = state_tax(amount)
  # Calculate the country tax
  country = country_tax(amount)
  # Calculate the total tax
  total = total_tax(state,country)

  #Display the results
  print('\nAmount of the purchase: $',format(amount,',.2f'))
  print('State tax: $',format(state,',.2f'))
  print('Country tax: $',format(country,',.2f'))
  print('Total sales tax: $',format(total,',.2f'))
  print('Total sales: $',format(amount + total,',.2f')) #Calculate total sales

# The get_amount function prompts the
# user to enter an amount of a purchase and it
# returns that value.
def get_amount():
  price = float(input("Enter amount of a purchase: "))
  return price

# The state_tax function accepts an amount
# as an argument and returns the state tax
# specified by STATE_TAX_PERCENTAGE.
def state_tax(amount):
  return amount * STATE_TAX_PERCENTAGE


# The country_tax function accepts an amount
# as an argument and returns the country tax
# specified by COUNTRY_TAX_PERCENTAGE.
def country_tax(amount):
  return amount * COUNTRY_TAX_PERCENTAGE

# The total_tax function accepts an state and country
# as arguments and returns the total tax
def total_tax(state,country):
  return (state + country)


# Call the main function.
main()