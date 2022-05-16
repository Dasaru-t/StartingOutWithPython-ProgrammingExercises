# 4. Unique Words

def main():
  
  # Open the text file for reading
  infile = open("text.txt","r")
  
  # Read the lines.
  lines = infile.readlines()
  
  # Close the file.
  infile.close()
  
  # Create a new set to store unique words
  myset = set()
  
  # Read each line
  for line in lines:
    # Read each word
    for word in line.split(): # Split word by space      
      myset.add(word) # Add words to the set
    
  # Print unique words
  print(myset)
  
main()