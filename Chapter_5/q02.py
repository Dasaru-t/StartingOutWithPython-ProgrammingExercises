# 2. Sales Tax Program Refactoring


# Create global variables.
purchase = 0
statetax = purchase * 0.05 
countrytax = purchase * 0.025
totaltax = countrytax + statetax

def main():
  # Get the purchase amount
  purchase = float(input('Enter amount of a purchase: '))
  print('\nAmount of the purchase: $',format(purchase,',.2f'))
  state_tax()
  country_tax()
  total_tax()
  print('Total sales: $',format(purchase + totaltax,',.2f'))

def state_tax():
  print('State tax: $',format(statetax,',.2f'))

def country_tax():
  print('Country tax: $',format(countrytax,',.2f'))

def total_tax():
  print('Total sales tax: $',format(totaltax,',.2f'))

# Call the main function.
main()