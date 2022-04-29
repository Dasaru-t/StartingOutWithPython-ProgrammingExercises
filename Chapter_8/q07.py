# 7. Character Analysis

def main():
  
  # Open the text.txt file for reading
  infile = open("text.txt","r")
  
  # Read the line.
  lines = infile.readlines()
  
  upper = 0
  lower = 0
  digits = 0
  space = 0
  
  for i in lines:
    print
    
    '''''
    for n in len(i):
      if i.isupper():
        upper += 1
    
    
  print(upper)
  
  '''''
    
main()
    