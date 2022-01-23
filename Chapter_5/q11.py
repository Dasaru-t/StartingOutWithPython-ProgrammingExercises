# 11. Math Quiz
import random

def main():

  #genarate two random numbers
  number_1, number_2 = random_numbers()

  #display numbers
  print("Add these numbers")
  print("\n ",number_1)
  print("+",number_2)

  #get user answer
  number_3 = int(input("Enter the right answer: "))

  #check answers
  chk_answer(number_1, number_2,number_3)

# The random_numbers function genarate two
# random numbers and returns it
def random_numbers():
  number_1 = random.randint(1,1000)
  number_2 = random.randint(1,1000)
  return number_1, number_2

# The chk_answer function accepts number_1, number_2 & number_3
# as arguments and returns Answer
def chk_answer(number_1, number_2,number_3):
  if number_1 + number_2 == number_3:
    print("Congratulations!! Your answer is correct.")
  else:
    print("You'r answer is incorrect!")
    print("The correct answer is",number_1 + number_2)

  return

# Call the main function.
main()