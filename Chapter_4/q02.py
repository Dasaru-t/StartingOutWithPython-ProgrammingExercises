# 2. Calories Burned

per_min = 4.2
print('Minutes','|','Calories burned')
print('-'*25)
for min in range(10,31,5):
  calorie = per_min * min
  print(min,'\t-\t',format(calorie,'.1f'),sep='')