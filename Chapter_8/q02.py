# 2. Sum of Digits in a String

def main():
  try:    
    # Get user inputs
    numbers = input("Enter a series of single-digit numbers: ")

    # Initialize an accumulator variable.
    total = 0

    for i in numbers:
      # Convert strings to int
      number = int(i)
      total += number

    # Display results
    print("Total:",total)
    
  # Exception to handle non-numerical inputs
  except ValueError:
    print("You can't enter letters. Try again!")
    # Call the main function 
    main()

# Call the main function     
main()