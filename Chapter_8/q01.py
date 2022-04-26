# 1. Initials

def main():
  
  # gets a string containing a person’s first, middle, and last names
  name = input("Enter person's name: ")
  
  # Split the string
  name_split = name.split()
  
  # Display the result.
  print("Your initials")
  
  # Display their first, middle, and last initials.
  for i in name_split:
    print(i[0].upper(),end=".")
    
# Call the main function 
main()