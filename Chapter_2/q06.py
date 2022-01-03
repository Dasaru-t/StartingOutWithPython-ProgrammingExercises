# 6. Sales Tax

amount = float(input('Enter the amount of purchase: '))
# 2.5% equal to 0.025 (2.5/100 = 0.025)
state_tax = amount * 0.05
country_tax = amount * 0.025
total_tax = state_tax + country_tax
total_amount = amount + total_tax


#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#\n - Causes output to be advanced to the next line.
#sep='' - #if you don't want a space printed between the items

print('\nPurchse amount: $ ', format(amount, ',.2f'),sep='')
print('State tax: $ ', format(state_tax, ',.2f'),sep='')
print('Country tax: $ ', format(country_tax, ',.2f'),sep='')
print('Total tax: $ ', format(total_tax, ',.2f'),sep='')
print('\nTotal amount: $ ', format(total_amount, ',.2f'),sep='')

