# 4. Morse Code Converter
# This program converts string to morse

def main():
  
  # Get user input
  string = input("Enter a string: ").upper()
  
  # Create two lists for conversion. each index will match in two lists.
  # Create a list with character
  character=[" ", ",", ".", "?", "0", "1", "2", "3", "4", "5", "6", "7",\
               "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", \
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", \
               "W", "X", "Y", "Z"]

  # Create a list with code
  morse=[" ", "--..--", ".-.-.-", "..--..", "-----", ".----", "..---", "...--", \
           "....-", ".....", "-....", "--...", "---..", "----.", ".-", "-...", "-.-.", \
           "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", \
           ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.-", "--.."]
  
  # Go through each character in user input
  for i in string:
    # Find the morse code for each character
    print(morse[character.index(i)],end=" ")
    
# Call the main function   
main()