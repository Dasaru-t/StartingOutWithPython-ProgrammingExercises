# 8. Random Number File Reader

def main():

  # Open the random_numbers_file for reading
  random_number_file = open("random_number.txt","r")

  # Initialize an accumulator to 0.0
  count = 0
  total = 0

  # Read the file
  for line in random_number_file:
    number = float(line)
    # calculate the total of the numbers
    total += number
    # Count the number of random numbers
    count += 1
    # Display the numbers
    print(number)

  # Display the total & number count
  print()
  print("Total: ",total)
  print("Number count: ",count)

  # Close the file.
  random_number_file.close()

# Call the main function.
main()