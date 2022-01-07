# 6. Magic Dates
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
year = int(input("Enter a two digit year: "))

print("\n",month,"/",day,"/",year)
if (month * day) == year:
  print("!!**Date is Magic**!!")
else:
  print("Date is not a magic..")