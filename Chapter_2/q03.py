# 3. Land Calculation
area = float(input("Enter the total square feet : "))
acres = area/43560

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
print("Your area in acres:",format(acres,'.2f'))

