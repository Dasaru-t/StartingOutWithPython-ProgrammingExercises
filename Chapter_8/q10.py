# 10. Most Frequent Character

def main():
    
  # Get user input as a sentence
  string = input("Enter a sentence: ").lower()

  # create an empty list to store each character and
  # occurence list to store how many time it is repeated 
  # with same shared-index.
  string_list = []
  occurence = []

  # Read each character
  for i in string:
    # first make sure it is not whitespace or any other character than alphabet and number
    # simply use isalnum() for alphabetical and numerical characters.
    if i.isalnum():
      # if it is not in the list append it to string_list
      if i not in string_list:
        string_list.append(i)
        # and place its first occurence
        occurence.append(1)

      # if it is ON THE LIST
      elif i in string_list:
        occurence[string_list.index(i)]+=1

  # Find the maximum value of occurence
  max_occ = max(occurence)

  # Display results
  # Get the index of it
  print("\nThe most frequently occuring letter is:",string_list[occurence.index(max_occ)])
  print("occurence:",max_occ)

  print("\nCharacters in sentence:\n",string_list)
  print("occurences:\n",occurence)

# Call the main function.  
main()