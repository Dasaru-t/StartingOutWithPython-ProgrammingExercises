# 19. Future Value

def main():

  # get values
  present = float(input("Enter the account’s present value: "))
  interest_rate = float(input("Enter the monthly interest rate: "))
  no_of_months = float(input("Enter the number of months money will be left in the account: "))

  #calculate future value
  future = future_value(present, interest_rate, no_of_months)

  #display results
  print("\nAccount’s future value is: $",format(future,",.2f"))

# The future_value function accepts present, interest_rate & no_of_months
# as arguments and returns future value
def future_value(present, interest_rate, no_of_months):
  future = present * (1 + interest_rate)**no_of_months
  return future

# Call the main function.
main()