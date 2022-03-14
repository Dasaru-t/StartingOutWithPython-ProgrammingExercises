# 2. File Head Display

# This program uses the for loop to read
# first five lines of the txt file.

def main():

  # get the file name
  file_name = input("Enter the file name: ")

  # Open the user file for reading
  user_file = open(file_name,"r")

  # Read the first 5 lines from the file
  for i in range(5):
    lines = user_file.readline()

    #strip the newline from the field
    lines = lines.rstrip("\n")

    # Display file content
    print(lines)

  # Close the file.
  user_file.close()

# Call the main function.
main()