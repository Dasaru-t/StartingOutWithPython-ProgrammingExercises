# This program demonstrates object pickling.
import pickle

def main():
  
  personal = {}

  
  again = "y"
  while again.lower() == "y":
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = int(input("Enter your weight"))
    
    personal[name] = [age,weight]
    
    again = input("Do you want to enter another('y for yes'): ")
    
    
  print(personal)
    
main()