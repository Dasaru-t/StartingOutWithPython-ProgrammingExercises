# 10. Golf Scores - read

def main():

  # Open the golf.txt file for reading
  golf_file = open("golf.txt","r")

  # Read the name field
  name = golf_file.readline()

  # Display the header
  print("Player Name","\tScore")
  print("-"*21)

  # If a field was read, continue processing.
  while name != "":
    # Read the Score field
    score = golf_file.readline()

    # Strip the newline from the name field
    name = name.rstrip("\n")
    # Convert score to int.
    score = int(score)
    # Display the records.
    print(name,"\t\t",score)

    # Read the name field for the next record.
    name = golf_file.readline()

  # Close the file.
  golf_file.close()

# Call the main function
main()
