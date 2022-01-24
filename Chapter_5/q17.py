# 17. Prime Numbers

def main():
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
  for n in range(2,number):
    if number % n == 0:
      status = False
    else:
      status = True

    # Returning Boolean Value
    return status

# Call the main function.
main()