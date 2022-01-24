# 18. Prime Number List

def main():

  print("A prime number is a number that is") 
  print("only evenly divisible by itself and 1\n")
  print("The prime numbers from 1 to 100 are listed below.")

  #display results
  for number in range(1,101):
    if is_prime(number):
      print(number)

  
# The is_prime function accepts number
# as arguments and returns boolean value
def is_prime(number):
  # determine whether number is prime or not
  # create a for loop structure so we can divide our number
  # to each number that is less than it.
  status = True
  # we set status to be True until it could be falsified. If it can be divided by any number
  # less than itself, status=False. 
  for n in range(2,number):
    if number % n == 0:
        status = False 
      
    # Returning Boolean Value
  return status

# Call the main function.
main()

# percentage is remainder option. If it is divided evenly by any number (except 1 and itself)
# it is not prime number so status=False