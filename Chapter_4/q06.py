# 6. Celsius to Fahrenheit Table

print("Celsius\tFahrenheit")
print("-"*19)

for c in range(21):
  fa = (9/5) * c + 32 #formula
  print(c,"\t",format(fa,'.2f'))    #string '.2f', is the format specifier, 
                                    #.2 specifies the precision and f specifies that the data type of the number we are formatting (float).

  
