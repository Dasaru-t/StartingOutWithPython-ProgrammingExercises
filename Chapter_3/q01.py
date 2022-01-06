# 1. Day of the Week

number = int(input("Enter a number in the range of 1 through 7: "))

# Nested Decision Structures and the if-elif-else Statement
if number >= 1 and number <= 7:
  if number == 1:
    day = "Monday"
  elif number == 2:
    day = "Tuesday"
  elif number == 3:
    day = "Wednesday"
  elif number == 4:
    day = "Thursday"
  elif number == 5:
    day = "Friday"
  elif number == 6:
    day = "Saturday"
  else:
    day = "Sunday"

  print(number,"is",day)

else:
  #\n - Causes output to be advanced to the next line.
  print("\nError!! Enter a number inside the range of 1 through 7")

  