# 7. Random Number File Writer

import random

def main():

  # Get user input
  count = int(input("How many random numbers do you want: "))

  # Open the random_number.txt file for writing
  random_number_file = open("random_number.txt","w")

  # Generate 500 random numbers & write it to the file
  for i in range(count):
    random_number = random.randint(1,500)
    random_number_file.write(str(random_number) + "\n")

  # Close the file.
  random_number_file.close()
  print("Data written to random_number.txt")

# Call the main function.
main()