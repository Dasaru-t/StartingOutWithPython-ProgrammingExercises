#9 Roulette wheel colors

#asks the user to enter a pocket number
number = int(input('Enter a pocket number from 0 - 36: ' ))

if number >= 0 and number <= 36:
  if number == 0:
    color = 'green'
  elif (number >= 1 and number <=10) or (number >= 19 and number <=28):
    if (number%2) == 0:
      color = 'black'
    else:
      color = 'red'
  elif (number >= 11 and number <=18) or (number >= 29 and number <=36):
    if (number%2) == 0:
      color = 'red'
    else:
      color = 'black'
      
  print('\nYour color for number',number,'is',color)
else:
  print('\nERROR! please enter number range of 0 through 36')