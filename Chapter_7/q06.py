# 6. Larger Than n

import random

# List_size is used as a constant for the
# size of the list.
LIST_SIZE = 6

def main():
  # Get user inputs
  number = user_input()

  # Create a list with random numbers
  my_list = create_list()

  # Get numbers larger than n 
  greater_than_n(my_list,number)


def user_input():

  n = int(input("Enter a number (1-100): "))
  
  return n


def create_list():

  # Create a list to hold random numbers
  my_list = []

  for count in range(LIST_SIZE):
    my_list.append(random.randint(1,100))

  print("Numbers in list -",my_list)

  return my_list


def greater_than_n(my_list,number):
  # Create a new list to hold values greater than n
  new_list=[]
  for values in my_list:
    if values > number:
      new_list.append(values)

  print("Numbers greater than",number,"-",new_list) 
    
# Call the main function
main()