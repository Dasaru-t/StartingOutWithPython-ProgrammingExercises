# 12. Population

# ask user to enter inputs
population = int(input("Starting number of organisms: "))
increase = float(input("Average daily increase(for example 30 for 30%): "))
days = int(input("Number of days to multiply: "))

# convert percentage for calculation
increase = increase/100

# print headings
print("\nDay Approximate\tPopulation")
print("-"*26)

for days in range(1,days+1):
  print(days,"\t",format(population,".2f"))
  population += (population * increase) 


  