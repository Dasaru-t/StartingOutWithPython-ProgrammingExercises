# 13. Shipping Charges

#asks the user to enter the weight of a package
weight = float(input("Enter the weight of the package(pounds): "))

if weight <= 2:
  rate = 1.50

elif weight <= 6:
  rate = 3.00

elif weight <= 10:
  rate = 4.00

else:
  rate = 4.75

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#\n - Causes output to be advanced to the next line.
print("\nShipping charges for",weight,"pounds package is $",format(rate * weight,'.2f'))