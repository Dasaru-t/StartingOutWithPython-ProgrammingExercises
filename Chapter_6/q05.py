# 5. Sum of Numbers

# This program reads all of the numbers 
# stored in the file and calculates their total.

def main():

  # Open the numbers file for reading
  numbers_file = open("numbers.txt","r")

  # Initialize an accumulator to 0.0
  total = 0.0

  # Read the file
  for line in numbers_file:
    number = float(line)
    total += number

  # Display the total
  print("Total: ",total)

  # Close the file.
  numbers_file.close()

# Call the main function.
main()