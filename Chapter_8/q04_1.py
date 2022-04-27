# 4_1. Morse Code Converter reverse
# This program converts morse to string
def main():
  
  # Get user input as morse code
  m_code = input("Enter the morse code: ")
  
  # Split the morse code
  m_code = m_code.split()
  
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
  
  # Go through each morse code in user input
  for i in m_code:
    # Find the character for each morse code
    print(character[morse.index(i)],end = ' ')
    
# Call the main function     
main()