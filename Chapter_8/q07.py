# 7. Character Analysis

def main():
  
  # Open the text.txt file for reading
  infile = open("text.txt","r")
  
  # Read the line.
  lines = infile.read().splitlines()
  
  upper = 0
  lower = 0
  digits = 0
  space = 0
  
  for line in lines:
    for ch in line:
      if ch.isupper():
        upper += 1
      elif ch.islower():
        lower += 1
      elif ch.isdigit():
        digits += 1
      elif ch.isspace():
        space += 1
        
  print(upper)
  print(lower)
  print(digits)
  print(space)
    
  
    
main()
    