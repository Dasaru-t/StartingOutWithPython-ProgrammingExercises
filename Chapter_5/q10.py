# 10. Feet to Inches

#Global costant
ONE_FOOT_INCHES = 12

def main():
  #Get values
  feet = float(input("Enter number of feet: "))

  #calculate inches
  inches = feet_to_inches(feet)

  #Display the results
  print(inches,"inches equal to",feet,"feets")

# The feet_to_inches function accepts feet
# as argument and returns inches
# specified by Global costant ONE_FOOT_INCHES
def feet_to_inches(feet):  
  inches = feet * ONE_FOOT_INCHES
  return inches
  
# Call the main function.
main()