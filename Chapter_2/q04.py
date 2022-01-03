# 4. Total Purchase

item1 = float(input('Enter item 1 price: '))
item2 = float(input('Enter item 2 price: '))
item3 = float(input('Enter item 3 price: '))
item4 = float(input('Enter item 4 price: '))
item5 = float(input('Enter item 5 price: '))

sub_total = item1 + item2 +item3 + item4 + item5
# 7% equal to 0.7 (7/100 = 0.23)
tax = sub_total * 0.07
total = sub_total + tax

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#\n - Causes output to be advanced to the next line.
print('\nYour sub total: $ ', format(sub_total , '.2f'))
print('Sales Tax 7% : $ ', format(tax , '.2f'))
print('Total price: $ ', format(total , '.2f'))

