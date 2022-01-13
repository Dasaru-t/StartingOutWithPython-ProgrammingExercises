# 13_1. Write a program that uses nested loops to draw this pattern

# *******
# ******
# *****
# ****
# ***
# **
# *


for row in range(8,1,-1):
  for col in range(row - 1):
    print("*",end='')  # using end to command that "Do not go to new line"
  print()