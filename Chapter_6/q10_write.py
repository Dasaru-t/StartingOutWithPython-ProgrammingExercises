# 10. Golf Scores - write

# This program read each player’s name and golf score as keyboard input,
# and then save these as records in a file named golf.txt.

def main():

  # Open the golf.txt file for writting
  golf_file = open("golf.txt","w")

  # Create a variable to control the loop
  another = "y"

  # Get each player's data and write it to 
  # the file
  while another != "n":
    name = input("Enter player's name: ")
    score = int(input("Enter player's score: "))

    # write the data as a record to the file
    golf_file.write(name + "\n")
    golf_file.write(str(score) + "\n")

    # Determine whether the user wants to add
    # another record to the file.
    another = input("Do you want to enter another: ")

  # Close the file.
  golf_file.close()
  print()
  print("Golf records written to golf.txt")

# Call the main function
main()