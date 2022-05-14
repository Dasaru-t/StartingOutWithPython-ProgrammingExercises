# This program demonstrates object pickling.
import pickle

# main function
def main():
  
  # Create an empty dictionary.
  personal = {}

  again = "y" # To control loop repetition
  
  # Get data until the user wants to stop.
  while again.lower() == "y":
    
    # Get data for a person
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = int(input("Enter your weight: "))
    
    # Store it in the dictionary.
    personal[name] = [age,weight]
    
    print()
    # Does the user want to enter more data?
    again = input("Enter more data? (y/n): ")
    
    
  # Open a file for binary writing.
  output_file = open('personal.dat','wb')
  
  # Pickle the dictionary.
  pickle.dump(personal,output_file)
  
  # Close the file.
  output_file.close()
  print()
  print("write personal data to the personal.dat file.")
  print(personal)
  
main()