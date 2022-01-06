# 4. Roman Numerals

number = int(input("Enter a number within the range of 1 through 10: "))

if number >= 1 and number <= 10:

  if number == 1:
    roman = "I"
  elif number == 2:
    roman = "II"
  elif number == 3:
    roman = "III"
  elif number == 4:
    roman = "IV"
  elif number == 5:
    roman = "V"
  elif number == 6:
    roman = "VI"
  elif number == 7:
    roman = "VII"
  elif number == 8:
    roman = "VIII"
  elif number == 9:
    roman = "IX"
  else:
    roman = "X"

  print("\nNumber",number,"equal to the roman number",roman)

else:
  print("\nError!! Enter a number between 1 - 10")