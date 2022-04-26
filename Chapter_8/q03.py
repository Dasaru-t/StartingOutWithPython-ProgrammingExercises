def main():

    # Get user input
    date = input("Enter a date (mm/dd/yyyy): ")
    
    # Split the string by "/"
    date_split = date.split("/")

    # Create a list with 12 months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
    
    # Display results
    print(months[int(date_split[0])-1]," ",date_split[1],",",date_split[2],".",sep="")
      
# Call the main function     
main()