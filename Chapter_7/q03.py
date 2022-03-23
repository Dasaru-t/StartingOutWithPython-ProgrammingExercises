# 3. Rainfall Statistics

# MONTHS is used as a constant for the
# size of the list.
MONTHS = 12

def main():
  # Create a variable to use as an accumulator.
  total = 0.0

  # Create a list to hold rainfall data
  rainfall_list = []

  # Get rainfall for each month
  for m in range(MONTHS):
    rainfall = float(input("Enter rainfall for month #" + str(m+1) +": "))
    rainfall_list.append(rainfall)

  # Calculate the total & the average
  for values in rainfall_list:
    total += values
    average = total / (len(rainfall_list))

  # Get minimum & maximum amounts
  minimum = min(rainfall_list)
  maximum = max(rainfall_list)  
  
  # Display the total,average of the list elements.
  print()
  print("Data you entered: ",rainfall_list,sep="")
  print("Total Rainfall: ",format(total,".2f"),sep="")
  print("Average Rainfall: ",format(average,".2f"),sep="")
  print("Highest Rainfall: ",format(maximum,".2f"),sep="")
  print("Lowest Rainfall: ",format(minimum,".2f"),sep="")

# Call the main function.
main()