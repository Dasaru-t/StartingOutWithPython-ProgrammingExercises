# 2. Sales Prediction

total_sales = float(input('Enter projected amount of total sales: $ '))

# 23% equal to 0.23 (23/100 = 0.23)
#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#to be formatted with comma separators, you can insert a comma into the format specifier.
print('Annual profit is: $',format(total_sales * 0.23, ',.2f'))