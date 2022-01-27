def main():
  # open a file for reading.
  infile = open('numbers.txt','r')

  # Read three numbers from the file.
  num1 = int(infile.readline())
  num2 = int(infile.readline())
  num3 = int(infile.readline())

  # close the file
  infile.close()

  # add the three numbers.
  total = num1 + num2 + num3

  # Display the numbers and their total.
  print("The numbers are:",num1, num2, num3)
  print('There total is:',total)

# call the main function
main()