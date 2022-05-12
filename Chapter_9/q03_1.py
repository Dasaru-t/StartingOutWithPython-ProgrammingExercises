# 3. File Encryption and Decryption
# File Decryption

def main():
  # Create dictionarie
  encrypt={'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
             'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
             'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
             'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
             'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
             't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q',' ':' ','.':'~~','\n':'\n'}

  # Open the d text.txt file for reading
  out_file = open("out_text.txt","r")

  # Read the lines.
  lines = out_file.readlines()
  
  # Close the file.
  out_file.close()
    
  print("Decrypted content: ")

  # For each sentence
  for line in lines:
    # For each character
    for ch in line:
      # Read encrypted content from the file 
      for i,j in encrypt.items():
        if j == ch:
          print(i,end='')
    
  print()
  
# Call the main function.
main()