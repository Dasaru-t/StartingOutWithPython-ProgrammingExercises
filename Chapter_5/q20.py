# 20. Random Number Guessing Game

import random
count = 1

def main():
  #display header
  print("Please try to guess random number from 1 through 100\n")
  print("Attempt no",count)

  #generate random number
  random_number = gen_random()

  # get user value
  user_number = int(input("Enter your number: "))

  number_guess(random_number, user_number)
  
#The gen_random function returns random number
def gen_random():
  random_number  = random.randint(1,100)
  return random_number

# The number_guess function accepts random_number & user_number
# as arguments and display results
def number_guess(random_number, user_number):
  # initialize an accumulator variable
  count = 1

  # if user unable to guess it with in 1 st attempt
  # following code will execute
  while random_number != user_number:  
    # compare user number & random number
    if random_number < user_number:
      print("Too high, try again.")
    else:
      print("Too low, try again.")
    
    print("Attempt no",count + 1)
    
    user_number = int(input("Enter your number again: "))
    count += 1 #counting user attempts
    
  #display results
  print("\nYou found the number",random_number)
  print("Congratulation! you correctly guess it after",count,"attempts")

# Call the main function.
main()