# 14. Write a program that uses nested loops to draw this pattern:

##
# #
#  #
#   #
#    #
#     #

base = 6
for row in range(base):
  print("#",end="") #every line start with #
  for col in range(row):
    print(" ",end = "") 
  print("#")    # every line finish with #
