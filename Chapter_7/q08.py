# 8. Name Search

def main():
  # Get file names and add it to a lists
  boynames, girlnames = file_open()

  # check names if they are in the list
  user_input(boynames, girlnames)


def file_open():
  # Open boys_file & girls_file for for reading.
  boys_file = open("BoyNames.txt","r")
  girls_file = open("GirlNames.txt","r")

  # Read the lines from both files
  boynames = boys_file.readlines()
  girlnames = girls_file.readlines()

  # Strip all the \n from the elements
  index = 0
  while index < len(boynames):
    boynames[index] = boynames[index].rstrip("\n")
    index += 1

  index = 0
  while index < len(girlnames):
    girlnames[index] = girlnames[index].rstrip('\n')
    index += 1

  # Returning values
  return boynames, girlnames


def user_input(boynames, girlnames):
  # Check names if they are in the list
  boy = input("Do you want to enter a boy name (y for yes):")
  if boy == "y":
    boy_name = input("Enter Boy name: ")

    # Search for boy name
    if boy_name in boynames:
      print(boy_name,"is among the most popular names.")
    else:
      print(boy_name,"is not a popular name.")

  girl = input("Do you want to enter a girl name (y for yes):")
  if girl == "y":
    girl_name = input("Enter Girl name: ")

    # Search for girl name
    if girl_name in girlnames:
      print(girl_name,"is among the most popular names.")
    else:
      print(girl_name,"is not a popular name.")

# Call the main function
main()