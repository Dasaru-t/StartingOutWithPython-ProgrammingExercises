# 6. Calories from Fat and Carbohydrates

def main():
  fat, carb = get_values()
  cal_f, cal_c = calc_calories(fat,carb)
  total = total_cal(cal_f, cal_c)
  print("\nCalories from fat :",cal_f)
  print("Calories from carbs :",cal_c)
  print("Total calories :",total)


def get_values():
  fat = int(input("Enter number of fat grams: "))
  carb = int(input("Enter number of carbohydrate grams: "))
  return fat, carb

def calc_calories(fat,carb):
  cal_f = fat * 9
  cal_c = carb * 4
  return cal_f, cal_c

def total_cal(cal_f, cal_c):
  return cal_f + cal_c
  
main()