# 12. Pig Latin

# This program accepts a sentence as input and converts each word to "Pig Latin."

# In one version, to convert a word to Pig Latin you remove the first letter and place that letter
# at the end of the word. Then you append the string “ay” to the word.

def main():
  
  # Get user input as a sentence
  sentence = input("Enter a sentence in English: ")

  # Split the string
  mylist = sentence.split()

  # Get length of the list
  length = len(mylist)

  #Create a new list
  mystring = []

  for i in range(length):
    # Remove the first letter
    # Place that letter at the end of the word
    # Add items to the new list
    # Append the string “ay”
    mystring.append(mylist[i][1:]+ mylist[i][0] + 'AY')

  # Concatenate list in to a single string  
  print("Pig Latin:"," ".join(mystring))
  
main()
