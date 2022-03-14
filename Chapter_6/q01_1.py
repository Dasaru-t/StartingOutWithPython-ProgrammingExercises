# 1_1. File Display

# This program uses the while loop to read
# all of the values in the numbers.txt file.

def main():
  # Open the numbers.txt file for reading
  numbers_file = open("numbers.txt","r")

  # Read the first line from the file, but
  # don't convert to a number yet. We still
  # need to test for an empty string.
  number = numbers_file.readline()

  # As long as an empty string is not returned 
  # from readline, continue processing
  while number != "":
      
    # Convert line to a float.
    number = int(number)
    
    # Display the number.
    print(number)

    # Read the next line.
    number = numbers_file.readline()

  # Close the file.
  numbers_file.close()

# Call the main function
main()
