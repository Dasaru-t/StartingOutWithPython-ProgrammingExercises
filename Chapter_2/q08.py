#8. Tip, Tax, and Total
food = float(input('Enter the charge for the food: $ '))

# 18% equal to 0.18 (18/100 = 0.18)
tip = food * 0.18
tax = food * 0.07
total = food + tip + tax

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#\n - Causes output to be advanced to the next line.
print('\nTip amount: $',format(tip,',.2f'))
print('Sales TAX amount: $',format(tax,',.2f'))
print('Total amount: $',format(total,',.2f'))