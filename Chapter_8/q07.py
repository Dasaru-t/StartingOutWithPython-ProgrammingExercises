# 7. Character Analysis

def main():
  
  # Open the text.txt file for reading
  infile = open("text.txt","r")
  
  # Read the line.
  lines = infile.readlines()
  
  # Close the file
  infile.close
  
  # Initialize an accumulator
  upper = 0
  lower = 0
  digits = 0
  space = 0
  
  # For each sentence
  for line in lines:
    # For each character
    for ch in line:
      if ch.isupper():
        upper += 1
      elif ch.islower():
        lower += 1
      elif ch.isdigit():
        digits += 1
      elif ch.isspace():
        space += 1
        
  # Display results
  print("The number of uppercase letters in the file:",upper)
  print("The number of lowercase letters in the file:",lower)
  print("The number of digits in the file:",digits)
  print("The number of whitespace characters in the file:",space)
   
 
# Call the main function    
main()