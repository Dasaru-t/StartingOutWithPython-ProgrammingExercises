# 8. Sentence Capitalizer

def main():
    
  # Get user input as a sentence
  string = input("Enter a sentence: ")

  # Split the sentence by ". "
  string_split = string.split(". ")

  for i in string_split:
    # first character of each sentence capitalized
    print(i[0].upper(),i[1:],sep="",end=". ")

# Call the main function   
main()
