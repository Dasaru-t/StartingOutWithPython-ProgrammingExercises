# 5. Alphabetic Telephone Number Translator

def main():
    
  # Get user input as a 10-character telephone number
  inputs = input("Enter a 10-character telephone number(XXX-XXX-XXXX): ").upper()

  # Create two lists for conversion. each index will match in two lists.
  # Create a list with letters
  letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
              'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

  # Create a list with numbers
  numbers = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

  # Go through each character in input
  for i in inputs:
    # If it is alphabetical convert it, or else keep it.
    if i.isalpha():
      print(numbers[letters.index(i)],end = "")
    else:
      print(i,end = "")

# Call the main function 
main()
