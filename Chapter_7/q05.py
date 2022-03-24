# 5. Charge Account Validation

def main():

  # convert to int & put it to a list
  number_list = into_a_list()
  #print(number_list)

  # Get user input
  c_number = int(input("Enter Charge account number: "))

  # Determine whether the number is valid
  number_valid(number_list,c_number)
  

def into_a_list():

  # Open charge_acc file for reading.
  charge_acc = open("charge_accounts.txt","r")

  # Read the contents of the file into a list.
  numbers = charge_acc.readlines()

  # Convert each element to an int.
  index = 0
  while index < len(numbers):
    numbers[index] = int(numbers[index])
    index += 1

  # Return the list 
  return numbers

def number_valid(number_list,c_number):

  if c_number in number_list:
    print("The number is valid")
  else:
    print("The number is not valid")

 
# call the main function
main()