# This program creates five CellPhone objects and
# stores them in a list.

import cellphone

def main():
    # Get a list of CellPhone objects.
    phones = make_list()

    # Display the data in the list.
    print('Here is the data you entered:')
    display_list(phones)

# The make_list function gets data from the user
# for five phones. The function returns a list
# of CellPhone objects containing the data. 

def make_list():
    # Create a empty list.
    phone_list = []

    # Add five CellPhone objects to the list.
    print('Enter data for five phones.')
    for count in range(1, 6):
        # Get the phone data.
        print('Phone number ' + str(count) + ": ")
        man = input('Enter the manufacturer: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the retail price: '))
        print()


