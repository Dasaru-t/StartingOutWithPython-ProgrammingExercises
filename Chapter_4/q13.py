# 13. Write a program that uses nested loops to draw this pattern

# *******
# ******
# *****
# ****
# ***
# **
# *

count = 7

for row in range(count):
  for col in range(count - row):
    print("*",end='')  # using end to command that "Do not go to new line"
  print()
  