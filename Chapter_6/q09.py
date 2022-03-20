# 9. Exception Handing

# This program reads all of the numbers 
# stored in the file and calculates their total & average.

def main():

  # Initialize an accumulator to 0.0
  total = 0.0
  count = 0

  try:
    # Open the numbers file for reading
    numbers_file = open("numbers.txt","r")

    # Read the file
    for line in numbers_file:
      number = float(line)
      count += 1
      total += number

    # Display the total
    print("Total:",total)
    print("Count:",count)
    # Calculate average 
    print("Average:",format(total/count,".2f"))

    # Close the file.
    numbers_file.close()

  except IOError:
    print('An error occured trying to read the file.')

  except ValueError:
    print('Non-numeric data found in the file.')

# Call the main function.
main()