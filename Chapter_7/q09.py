# 9. Population Data

def main():
  population_list = into_a_list()
  print(population_list)

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

  return population_list


main()