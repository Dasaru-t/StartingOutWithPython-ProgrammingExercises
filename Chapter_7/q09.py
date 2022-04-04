# 9. Population Data

def main():

  # Convert to int & put it to a list
  population_list = into_a_list()
  # Calculate annual change
  ac_list,ac_avg, ac_max, ac_min = calc_population(population_list)

  print("The average annual change in population during 1950 and 1990 is",format(ac_avg,",.2f"))
  print("The year with the greatest increase is",ac_list.index(ac_max)+(1950 + 1),"with & increase of",ac_max)
  print("The year with the smallest increase is",ac_list.index(ac_min)+(1950 + 1),"with & increase of",ac_min)

  print()
  print("  Years\t\tAnnual Change")
  print("-"*30)
  count = 0
  for numbers in ac_list:
    print(1950 + count,"-",1951 + count,"\t\t",numbers)
    count+=1


def into_a_list():
  # Open USPopulation file for reading.
  populaion_file = open("USPopulation.txt","r")

  # Read the lines from USPopulation file
  population_list = populaion_file.readlines()

  # Convert each element to an int.
  index = 0
  while index < len(population_list):
    population_list[index] = int(population_list[index])
    index += 1

  # Return the list
  return population_list


def calc_population(population):

  # Create an empty list
  annual_change = [0] * (len(population)-1)
  
  # Calculate annual change. Example (year 2 - year 1)
  index = 0

  # Since there are 41 years, there will be 40 annual change
  # excluding first year.
  while index < len(population) -1:
    annual_change[index] = population[index + 1]-population[index]
    index += 1

  # Calculate the total of annual change
  total = 0
  for i in annual_change:
    total += i

  # Calculate the average
  annual_change_avg = total / len(annual_change)
  # Find the greatest value
  annual_change_max = max(annual_change)
  # Find the smallest value
  annual_change_min = min(annual_change)

  # Returning values
  return annual_change,annual_change_avg, annual_change_max, annual_change_min

# Call the main function
main()