# 6. Calories from Fat and Carbohydrates

def main():
  #Get the values
  fat, carb = get_values()

  #Calculate calories for fat & carbs
  cal_f, cal_c = calc_calories(fat,carb)

  #Calculate total
  total = total_cal(cal_f, cal_c)

  #Display the results
  print("\nCalories from fat :",cal_f)
  print("Calories from carbs :",cal_c)
  print("Total calories :",total)

# The get_values function prompts the
# user to enter the fat grams & carbs and it
# returns that values.
def get_values():
  fat = int(input("Enter number of fat grams: "))
  carb = int(input("Enter number of carbohydrate grams: "))
  return fat, carb

# The calc_calories function accepts fat & carb
# as an arguments and returns the cal_f & cal_c
def calc_calories(fat,carb):
  cal_f = fat * 9
  cal_c = carb * 4
  return cal_f, cal_c

# The total_cal function accepts fat & carb
# as an arguments and returns total amount
def total_cal(cal_f, cal_c):
  return cal_f + cal_c

# Call the main function.  
main()