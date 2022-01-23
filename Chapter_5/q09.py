# 9. Monthly Sales Tax

#Global costant
STATE_SALES_TAX = 0.05
COUNTRY_SALES_TAX = 0.025

def main():
  #Get values
  total_sales = get_value()

  #Calculate county sales tax, state sales tax & Total tax
  c_sales_tax,s_sales_tax,total_tax = tax_calc(total_sales)

  #Display the results
  print("\nThe amount of county sales tax: $",format(c_sales_tax,",.2f"))
  print("The amount of state sales tax: $",format(s_sales_tax,",.2f"))
  print("The total sales tax: $",format(total_tax,",.2f"))

# The get_value function prompts the
# user to enter the total sales and it
# returns that value
def get_value():
  total_sales = float(input("Enter the total sales for the month :"))
  return total_sales

# The tax_calc function accepts total_sales
# as arguments and returns county sales tax, state sales tax & Total tax
# specified by Global costant STATE_SALES_TAX, COUNTRY_SALES_TAX
def tax_calc(total_sales):
  c_sales_tax = total_sales * COUNTRY_SALES_TAX
  s_sales_tax = total_sales * STATE_SALES_TAX
  total_tax = c_sales_tax + s_sales_tax
  return c_sales_tax,s_sales_tax,total_tax

# Call the main function.
main()