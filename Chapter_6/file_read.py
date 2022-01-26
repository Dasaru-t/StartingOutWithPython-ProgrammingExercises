# This program reads and displays the contents
# of the philosophers.txt file.

def main():
  # Open a file named philosophers.txt.
  infile = open('philosophers.txt','r')

  # Read the file's contents.
  file_contents = infile.read()

  # close the file.
  infile.close()

  # print the data that was read into
  # memory
  print(file_contents)

# call the main function.
main()