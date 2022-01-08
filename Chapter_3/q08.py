# 8. Hot Dog Cookout Calculator

people = int(input("Enter number of people attending: "))
each_per = int(input("Enter number of hot dogs each person will be given: "))

#calculate the total hotdogs
total = people * each_per

# create decision structure.
# case 1. No leftover for hot dogs and buns; divided by both 10 and 8.
if total%10==0 and total%8==0:
  print("You will need", (total//10),"packs of hot dogs and",total//8,"packs of buns.")
  print("There will be no left overs.")

# case 2. left over for hot dogs but no buns.
elif total%10!=0 and total%8==0:
  print("You will need", (total//10)+1, "packs of hot dogs and", total//8, "packs of buns.")
  print("There will be", 10-(total%10), "hot dogs leftover.")

# case 3. left over for buns, but not hot dogs
elif total%10==0 and total%8!=0:
  print("You will need", total//10, "packs of hot dogs and", (total//8)+1, "packs of buns.")
  print("There will be", 8-(total%8), "buns leftover.")

# case 4 both leftover.
else:
  print("You will need", (total//10)+1, "packs of hot dogs and", (total//8)+1, "packs of buns.")
  print("There will be", 10-(total%10), "hot dogs leftover and ", 8-(total%8), "buns leftover.")



