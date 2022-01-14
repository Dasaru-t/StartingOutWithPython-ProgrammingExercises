# 9. Ocean Levels

ml = 0.0    # Initialize an accumulator variable.
start_year = 2022
end_year = 2047

# print headings
print("year\tNumber of ml")
print("-"*20)

for year in range(start_year,end_year):
  ml += 1.6 #ocean’s level is currently rising at about 1.6 millimeters per year
  print(year,"\t",format(ml,".2f")) # string '.2f', is the format specifier, 
                                    #.2 specifies the precision and f specifies that the data type of the number we are formatting (float)
