# 21. Rock, Paper, Scissors Game
import random

def main():
  # display header
  print("1 = Rock\n","2 = Paper\n","3 = Scissors\n",sep="")

  # create a variable to control the loop.
  status = True
  while status == True:    

    # generate random number
    random_number = gen_random()

    # get user input
    user_number = int(input("Enter you'r choice: "))
    print()

    user_choice(user_number)
    computer_choice(random_number)
    print()

    #determine the winner
    status = game_play(random_number, user_number)
    
# generate random number & return it
def gen_random():
  random_number = random.randint(1,3)
  return random_number

# determine & display user choice
def user_choice(user_number):
  if user_number == 1:
    print("You choose Rock")
  elif user_number == 2:
    print("You choose Paper")
  elif user_number == 3:
    print("You choose Scissors")
  else:
    print()
  
# determine & display computer choice
def computer_choice(random_num):
  if random_num == 1:
    print("Computer choose Rock")
  elif random_num == 2:
    print("Computer choose Paper")
  else:
    print("Computer choose Scissors")
  
# The game_play function accepts random_number and user_number
# as arguments and returns future value  
def game_play(random_number, user_number):

  status = False # to stop while loop
  # if user enter a invalid number
  if user_number == 1 or user_number == 2 or user_number == 3: 

    if user_number == 1 and random_number == 2:         
      print("Computer wins!")
      print("Paper wraps rock.")
    elif user_number == 1 and random_number == 3:
      print("You wins!")
      print("The rock smashes the scissors.")
    elif user_number == 2 and random_number == 1:
      print("You wins!")
      print("Paper wraps rock.")
    elif user_number == 2 and random_number == 3:
      print("computer wins!")
      print("Scissors cuts paper.")
    elif user_number == 3 and random_number == 1:
      print("Computer wins!")
      print("The rock smashes the scissors.")
    elif user_number == 3 and random_number == 2:
      print("You wins!")
      print("Scissors cuts paper.")
    elif user_number == random_number:
      print("Both players make the same choice")
      print("The game must be played again to determine the winner.")
      # If both players make the same choice, 
      # the game must be played again to determine
      # the winner.
      status = True # to run while loop again

  else:
    # if user enter a invalid number
    # it wil display this
    print("But you enter a")
    print("invalid number! Enter 1 = Rock, 2 = Paper or 3 = Scissors")

  #return status value back to while loop
  #at main function
  return status
      
# Call the main function.   
main()