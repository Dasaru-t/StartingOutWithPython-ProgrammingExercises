#12. Stock Transaction Program

no_shares_p = 2000                      #number of shares that Joe purchased
share_price_p = 40.00                   #Per share price when Joe purchased the stock
total_p = no_shares_p * share_price_p   #amount of money Joe paid for the stock
commission_p = total_p * 0.03           #amount of commission Joe paid his broker when he bought the stock
profit_p = total_p + commission_p       #Total cost for pruchase

no_shares_s = 2000                      #number of shares that Joe sold
share_price_s = 42.75                   #Per share price when Joe sold the stock
total_s = no_shares_s * share_price_s   #amount that Joe sold the stock for
commission_s = total_s * 0.03           #amount of commission Joe paid his broker when he sold the stock
recived_amount = total_s - commission_s #Joe recived amount

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
#to be formatted with comma separators, you can insert a comma into the format specifier.
#\n - Causes output to be advanced to the next line.

print("\nThe amount of money Joe paid for the stock: $",format(total_p,',.2f'))
print("The amount of commission Joe paid his broker when he bought the stock: $",format(commission_p,',.2f'))
print("\nThe amount that Joe sold the stock for: $",format(total_s,',.2f'))
print("The amount of commission Joe paid his broker when he sold the stock: $",format(commission_s,',.2f'))
print("\nTotal cost for pruchase: $",format(profit_p,',.2f'))
print("Recived amount: $",format(recived_amount,',.2f'))
print("Joe made a (+)profit/(-)loss of: $",format(recived_amount - profit_p,',.2f'))

