# This program unpickles CellPhone objects.
import pickle
import cellphone

# Constant for the filename.
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False # To indicate end of file

    # Open the file.
    input_file = open(FILENAME, 'rb')

    # Read to the end of the file.
    while not end_of_file:
        try:
            # Unpickle the next object.
            phone = pickle.load(input_file)

            # Display the cell phone data.
            display_data(phone)
        except EOFError:
            # Set the flag to indicate the end
            # of the file has been reached.
            end_of_file = True
