# 12. Maximum of Two Values

def main():
  print("This program returns the greater value!")

  #Get values
  number_1 = int(input("Enter a integer value: "))
  number_2 = int(input("Enter another integer value: "))

  #compare two numbers
  max_(number_1, number_2)

# The max_ function accepts number_1 & number_2
# as argument and returns greater number
def max_(number_1, number_2):
  if number_1 > number_2:
    print(number_1,"is greater than",number_2)
  elif number_2 > number_1:
    print(number_2,"is greater than",number_1)
  else:
    print("Both numbers are same.")
    print("Enter a different number!")

# Call the main function.
main()