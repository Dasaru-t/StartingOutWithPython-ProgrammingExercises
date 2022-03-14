# 3. Line Numbers

# This program display the contents of the file with 
# each line preceded with a line number followed by a colon.

def main():

  # get the file name
  file_name = input("Enter the file name: ")

  # Open the user file for reading
  user_file = open(file_name,"r")

  # Initialize an accumulator to 0
  number = 0

  # Read the first 5 lines from the file
  for line in user_file:
    
    #strip the newline from the field
    line = line.rstrip("\n")

    # increase the line numbering by 1
    number += 1

    # Display line number with colon
    print(number,":",sep="",end="")
    # Display file content
    print(line)
    
  # Close the file.
  user_file.close()

# Call the main function.
main()