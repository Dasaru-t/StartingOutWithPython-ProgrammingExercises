# 17. Prime Numbers

def main():

  print("A prime number is a number that is") 
  print("only evenly divisible by itself and 1\n")
  #get value
  number = int(input("Enter a number: "))

  #display results
  if is_prime(number):
    print(number, "is a Prime number")
  else:
    print(number,"is not a prime number")

# The is_prime function accepts number
# as arguments and returns boolean value
def is_prime(number):
  
  #determine whether number is prime or not
  status = True
  for n in range(2,number):
    if number % n == 0:
        print(number,"can be divided by",n)
        status = False 
      
    # Returning Boolean Value
  return status

# Call the main function.
main()