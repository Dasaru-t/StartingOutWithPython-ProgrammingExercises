#4. Number Analysis Program

# NUMBERS is used as a constant for the
# size of the list.
NUMBERS = 20

def main():
  # Create a variable to use as an accumulator.
  total = 0.0

  # Create a list to hold numbers
  numbers_list = []

  # Display header
  print("Enter a series of",NUMBERS,"numbers: ")

  # Get 20 numbers
  for n in range(NUMBERS):
    number = float(input("Number #"+str(n + 1)+" : "))
    numbers_list.append(number)
  print()
  
  # Calculate the total
  for t in numbers_list:
    total += t
    
  # Get highest,lowest & average amounts
  lowest = min(numbers_list)
  highest = max(numbers_list)
  length = len(numbers_list)

  average  = total / length

  # Display the results
  print("Numbers you entered:",numbers_list)
  print("Lowest number: ",lowest)
  print("Highest number: ",highest)
  print("Total of the numbers: ",format(total,".2f"))
  print("Average of the numbers",format(average,".2f"))

# Call the main function.
main()