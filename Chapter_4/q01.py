#1. Bug Collector

# Initialize an accumulator variable.
total = 0

# Get the numbers and accumulate them.
for day in ['Monday','Tuesday','Wednsday','Thursday','Friday']:
  bugs = int(input("Enter the number of bugs collected for " +day+" : "))
  total += bugs   #Augmented assignment operators. equal to (total = total + bugs)

print('\nTotal number of bugs collected: ',total)

