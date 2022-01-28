# In the Spotlight: Searching for a Record

# This program allows the user to search the
# coffee.txt file for records matching a
# description.

def main():
  # create a bool variable to use a flag
  found = False

  # Get the search value.
  search = input('Enter a description to search for: ')

  # Open the coffee.txt file.
  coffee_file = open('coffee.txt','r')

  # Read the first record's description field.
  descr = coffee_file.readline()

  # Read the rest of the file.
  while descr != '':
    # Read the quantity field.
    qty = float(coffee_file.readline())

    # Strip the \n from the description.
    descr = descr.rstrip('\n')

    # Determine whether this record matches
    # the search value.
    if descr == search:
      # Display the record.
      print('Description:', descr)
      print('Quantity:', qty)
      print()
      # Set the found flag to True.
      found = True

    # Read the next description.
    descr = coffee_file.readline()

  # close the file
  coffee_file.close()

  # If the search value was not found in the file
  # display a message.
  if not found:
    print('That item was not found in the file.')

# call the main function
main()