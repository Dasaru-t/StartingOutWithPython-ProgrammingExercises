#7 color mixer
print('Primary colors : red, blue, yellow')

color1 = input('\nEnter a primary color 1: ')
if color1 != 'red' and color1 != 'blue' and color1 != 'yellow': 
  print('\nenter valid Primary color for 1st variable(red, blue, yellow)')
else:
  color2 = input('Enter a primary color 2: ')

  if (color2 != 'red' and color2 != 'blue' and color2 != 'yellow'):
    print('\nenter valid Primary color for 2nd variable(red, blue, yellow)')
  else:
    if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
      print(color1, '+', color2, '=','purple')    
    elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
      print(color1, '+', color2, '=','orange')    
    elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
      print(color1, '+', color2, '=','green')     
    else:
      print("\n",color1,"+",color1,"=",color1)
