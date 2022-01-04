#11. Male and Female Percentages
males = int(input("Enter number of the males registered in a class: "))
females = int(input("Enter number of the females registered in a class: "))

total = males + females
males_per = (males / total) * 100
females_per = (females / total) * 100

#\n - Causes output to be advanced to the next line.
#sep='' - #if you don't want a space printed between the items
#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
print("\nPercentage of males in the class: ",format(males_per,'.2f'),"%",sep = '')
print("Percentage of females in the class: ",format(females_per,'.2f'),"%",sep ='')