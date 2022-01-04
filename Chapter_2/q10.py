#10. Ingredient Adjuster

cookies = float(input('How many cookies do you want: '))

sugar = 1.5 * (cookies/48)
butter = 1 * (cookies/48)
flour = 2.75 * (cookies/48)

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#\n - Causes output to be advanced to the next line.
print('\nIngredients need for',cookies,'cookies')
print('\nSugar: ',format(sugar,'.2f'),'cups')
print('butter: ',format(butter,'.2f'),'cups')
print('flour: ',format(flour,'.2f'),'cups')

