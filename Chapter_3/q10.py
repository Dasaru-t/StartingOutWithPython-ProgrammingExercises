# 10. Money Counting Game

# 100 pennies = 1 $
# 20 nickels = 1 $
# 10 dimes = 1 $
# 4 quarters = 1 $

print('Enter the number of coins required to make 1$')
pennies = int(input("enter the number of pennies you have: "))
nickels = int(input("enter the number of nickels you have: "))
dimes = int(input("enter the number of dimes you have: "))
quarters = int(input("enter the number of quarters you have: "))

# convert all coin values to pennies (1$ equal to 100 pennies)
total = (pennies * 1) + (nickels * 5) + (dimes * 10) + (quarters * 25)
dollar = 100

if total == dollar:
  print("\nCongratulations!! you are the winner.")
  print("You entered",pennies,"Pennies +",nickels,"Nickels +",dimes,"Dimes +",quarters,"Quarters = 1 $")
  
elif (dollar - total) > 0:
  print("\nYou entered",pennies,"Pennies +",nickels,"Nickels +",dimes,"Dimes +",quarters,"Quarters")
  print("it's",(dollar - total),"Less pennies than $1." )

else:
  print("\nYou entered",pennies,"Pennies +",nickels,"Nickels +",dimes,"Dimes +",quarters,"Quarters")
  print("it's",(total - dollar),"more pennies than $1.")
  
