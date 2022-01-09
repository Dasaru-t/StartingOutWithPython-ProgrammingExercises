# 12. Software Sales

#asks the user to enter the number of packages purchased
packages = int(input("Enter the number of packages purchased: "))

price = 99

if packages < 10:
  discount = 0

elif packages >= 10 and packages <=19:
  discount = 0.1

elif packages >= 20 and packages <=49:
  discount = 0.2

elif packages >= 50 and packages <=99:
  discount = 0.3

else:
  discount = 0.4

amount = price * packages
discount_amount = amount * discount
after_dis = amount - discount_amount

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#\n - Causes output to be advanced to the next line.
print("\nTotal amount: $",format(amount,",.2f"),\
    "\nDiscount: $",format(discount_amount,",.2f"),\
        "\nNet total: $",format(after_dis,",.2f"))
