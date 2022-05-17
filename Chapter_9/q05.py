# Word Frequency

def main():
  
  # Set an accumulator
  index = 0
  total = 0

  # Open the d text.txt file for reading
  infile = open("in_text.txt","r")

  # Read the lines.
  lines = infile.readlines()
  
  # Close the file.
  infile.close()
  
  print("Text file content: ")
  
  # Create a new set to store unique words
  myset = set()
  
  mylist = []

  # For each sentence
  for line in lines:
    # For each character
    for word in line.split():
      myset.add(word) # Add words to the set
      mylist.append(word)
      
  mysetlist = list(myset)
    
  # Print unique words
  print(mysetlist)
  print("\n",mylist)
    
main()