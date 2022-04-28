# 6. Average Number of Words

def main():
  
  # Open the text.txt file for reading
  infile = open("text.txt","r")
  
  # Read the lines.
  lines = infile.readlines()
  
  # Initialize an accumulator
  line_count = 0
  total_word_count = 0
  
  for line in lines:
    # Count sentences
    line_count += 1
    
    # Count words
    word_count = len(line.split())
    total_word_count += word_count
  
  # Calculate the average
  avg = total_word_count / line_count
    
  # Display results
  print("Average number of words per sentence:",format(avg,".2f"))
  
  # Close the file.
  infile.close()

# Call the main function
main()