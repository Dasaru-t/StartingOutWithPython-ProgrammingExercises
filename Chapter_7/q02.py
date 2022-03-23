# 2. Lottery Number Generator
import random

# NUMBERS is used as a constant for the
# size of the list.
NUMBERS = 7

def main():

  # Generate random numbers
  my_list = random_numbers()

  # Display the random numbers.
  for values in my_list:
    print(values)


def random_numbers():

  # Create a list to hold values
  my_list = [0]*NUMBERS

  # Fill the list with random numbers.
  for n in range(NUMBERS):
    my_list[n] = random.randint(0,9)

  # Returning the list
  return my_list

# Call the main function.
main()