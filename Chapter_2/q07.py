#7. Miles-per-Gallon

#MPG = Miles driven Gallons of gas used

miles = float(input('Enter number of miles driven: ')) 
gallons = float(input('Enter number of gallons used: '))
mpg = miles / gallons

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#\n - Causes output to be advanced to the next line.
print('\nMiles per gallons: ', format(mpg, '.2f'))

