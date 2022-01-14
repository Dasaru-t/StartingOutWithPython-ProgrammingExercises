# 5. Average Rainfall

#ask for the number of years
years = int(input("Enter number of years: "))

months = 12
total = 0   # Initialize an accumulator variable.

for y in range(years):
  for m in range(months):
    rainfall = float(input("Inches of rainfall for year "+str(y + 1)+" month "+str(m + 1)+" : ")) #ask for the inches of rainfall for that month.
    total += rainfall #calculating running total
  print()

#Calculating duration in months & average rainfall
duration_in_months = months * years 
average_rainfall = total / duration_in_months

# Display the results
print("\nNumber of months:",duration_in_months)
print("Total inches of rainfall:",format(total,".2f"))
print("Average rainfall per month",format(average_rainfall,".2f"))