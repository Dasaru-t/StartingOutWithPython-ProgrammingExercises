# 1. File Display

# This program uses the for loop to read
# all of the values in the numbers.txt file.

def main():
  # Open the write.txt file for reading.
  numbers_file = open('numbers.txt', 'r')

  # Read all the lines from the file.
  for line in numbers_file:
    # Convert line to a int.
    number = int(line)
    # display the number.
    print(number)

  # Close the file.
  numbers_file.close()

 # Call the main function.
main()