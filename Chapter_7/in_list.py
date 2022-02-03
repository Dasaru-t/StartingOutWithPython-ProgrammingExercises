# in_list.py
# In the general format, item is the item for which you are searching, and list is a list. 
# The expression returns true if item is found in the list or false otherwise.

# This program demonstrates the in operator
# used with a list.

def main():
  # Create a list of product numbers.
  prod_nums = ['V475', 'F987', 'Q143', 'R688']

  # Get a product number to search for.
  search = input('Enter a product number: ')

  # Determine whether the product number is in the list.
  if search in prod_nums:
    print(search, 'was found in the list.')
  else:
    print(search, 'was not found in the list.')

# call the main function
main()