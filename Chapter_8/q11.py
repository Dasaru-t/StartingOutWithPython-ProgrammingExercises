# 11. Word Separator

def main():
    print("Example: StopAndSmellTheRoses\n")
    
    # Get user input as a sentence
    string=input("Enter a string like one above: ")   

    # Separate it by uppercase letter.
    # First letter would be capital
    print (string[0].upper(), end="")
    
    # Since we skip first letter, index=1
    index=1
    while index<len(string):
        if string[index].isupper():
            print(" ", end="")
            print(string[index].lower(), end="")
        else:
            print(string[index].lower(), end="")
        index+=1   
    print(".")
    
# Call the main function
main()