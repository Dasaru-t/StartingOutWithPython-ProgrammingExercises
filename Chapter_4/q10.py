# 10. Tuition Increase

tution = 8000.0
increase_by = 0.03
forecast_time = 5

# print headings
print("Year\tAmount")
print("-"*18)

# create loop structure
for year in range(1,forecast_time + 1):
  per_year = tution * increase_by 
  tution += per_year
  print(year,"\t$",format(tution,",.2f"))