# 10. World Series Champions

def main():

  # Convert to int & put it to a list
  wswinners_list = into_a_list()

  # Display Team names
  unique_names(wswinners_list)

  # Get team name
  team_name = input("Enter the name of the team: ")

  # Set an accumulator
  index = 0
  total = 0
  # Finding user input in list
  while index < len(wswinners_list):
    if wswinners_list[index] == team_name:
      total+=1
    index+=1

  # Display results
  print(team_name,"has been winner",total,"times.")


def into_a_list():

  # Open WorldSeriesWinners file for reading.
  wswinners_file = open("WorldSeriesWinners.txt","r")

  # Read the lines from WorldSeriesWinners file
  wswinners_list = wswinners_file.readlines()

  # Strip all the \n from the elements
  index = 0
  while index < len(wswinners_list):
    wswinners_list[index] = wswinners_list[index].rstrip('\n')
    index +=1 

  # Return the list
  return wswinners_list

  
def unique_names(wswinners_list):

  print("This program displays the number of times\
 that team \nhas won the World Series in the time period \nfrom 1903 through 2009.\n")
  
  # Get unique team names
  uni_names =list(set(wswinners_list))

  # Display teams
  print("Team list")  
  print("---------")
  index = 0
  while index < len(uni_names):
    print(uni_names[index])
    index+=1

  print()
  
main()