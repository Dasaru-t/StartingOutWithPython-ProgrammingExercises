# 14. Write a program that uses nested loops to draw this pattern:

##
# #
#  #
#   #
#    #
#     #


for row in range(6):
  for col in range(1):
    print("#"," "*row,end = "") #every line start with #
  print("#")    # every line finish with #
