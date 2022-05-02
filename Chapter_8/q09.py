# 9. Vowels and Consonants

def main():
    
  # Get user input as a sentence
  string = input("Enter a sentence: ").lower()
  
  vow,con = vowelsandconsonants(string)
  
  # Display results
  print("Length of the sentence:",len(string))
  print("Number of vowels:",vow)
  print("Number of consonants:",con - vow)
    
  
def vowelsandconsonants(string):
  # create a list for vowel
  vowels_list = ["a","e","i","o","u"]
  
  # Initialize an accumulator
  vowels = 0
  consonants = 0
  
  # Read each character
  for i in string:
    if i.isalpha():
      consonants += 1
      if i in vowels_list:
        vowels += 1
        
  # Return values
  return vowels, consonants
      
# Call the main function.    
main()