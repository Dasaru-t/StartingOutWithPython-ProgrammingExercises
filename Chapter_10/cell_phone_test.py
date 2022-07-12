# cell_phone_test.py
# This program tests the CellPhone class.

def main():
    # Get the phone data.
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))

    # Create an instance of the CellPhone class.
    phone = cellphone.CellPhone(man, mod, retail)

    # Display the data that was entered.
    print('Here is the data that you entered:')
    
    print('Manufacturer:', phone.get_manufact())
