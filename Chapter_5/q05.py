# 5. Property Tax

#Global costant
ASSESSMENT_VALUE_PERCENTAGE = 0.6
PROPERTY_TAX = 0.72 #cents

def main():
  #Get the actual value
  actual_value = get_value()

  #Calculate the Assessment value
  a_value = assessment_value(actual_value)

  #Calculate the property tax
  p_tax = property_tax(a_value)

  #Display the results
  print("\nAssessment value of property is: $",format(a_value,",.2f"))
  print("The property tax is: $",format(p_tax,",.2f"))

# The get_value function prompts the
# user to enter the actual value and it
# returns that value.
def get_value():
  value = float(input("Enter the actual value of a property: "))
  return value

# The assessment_value function accepts a_value
# as an argument and returns the assessment value
# specified by ASSESSMENT_VALUE_PERCENTAGE.
def assessment_value(actual_value):
  return actual_value * ASSESSMENT_VALUE_PERCENTAGE

# The property_tax function accepts a_value
# as an argument and returns the property tax amount
def property_tax(a_value):
  cost = a_value / 100   #72¢ for each $100
  return cost * PROPERTY_TAX

# Call the main function.
main()