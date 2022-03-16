# 4. Item Counter

# This program displays the number of names that 
# are stored in the file.

def main():
  # Open the names file for reading
  names_file = open("names.txt","r")

  # Initialize an accumulator to 0
  number = 0

  # Read the first record
  name = names_file.readline()

  # Count other names
  while name != "":
    # Increase the count by 1
    number += 1

    # Read the next record
    name = names_file.readline()

  # Display results
  print("There are",number,"names in names.txt file")

  # Close the file.
  names_file.close()

# Call the main function.
main()
