# If you want to have just one except clause to catch all the exceptions
# are raised in a try suite, you can specify Exception as the type.
# sales_report3.py

# This program displays the total of the
# amounts in the sales_data.txt file.

def main():
  # Initialize an accumulator.
  total = 0.0

  try:
    # Open the sales_data.txt file.
    infile = open('sales_data.txt','r')

    # Read the values from the file and
    # accumulate them.
    for line in infile:
      amount = float(line)
      total += amount

    # Close the file
    infile.close()

    # Print the total.
    print(format(total, ',.2f'))

  except Exception as err:
    print(err)

# Call the main function
main()