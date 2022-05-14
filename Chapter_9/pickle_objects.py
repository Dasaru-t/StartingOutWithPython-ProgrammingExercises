# This program demonstrates object pickling.
import pickle
def main():
  
  personal = {}

  
  again = "y"
  while again.lower() == "y":
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = int(input("Enter your weight: "))
    
    personal[name] = [age,weight]
    
    print()
    again = input("Do you want to enter another('y for yes'): ")
    
    
  output_file = open('personal.dat','wb')
  pickle.dump(personal,output_file)
  output_file.close()
  print()
  print("write personal data to the personal.dat file.")
  print(personal)
  
    
main()