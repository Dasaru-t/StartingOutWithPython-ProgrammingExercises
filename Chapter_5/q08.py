# 8. Paint Job Estimator

#Global costant
PER_GALLON = 112
LABOR_HOURS = 8
PER_HOUR_LABOR_CHARGE = 35.00

def main():
  #Get values
  wall_space, paint_price = get_values()

  #Calculate number of gallons & cost of the paint
  gallons_of_paint, paint_cost = paint_calc(wall_space, paint_price)

  #Calculate hours of labor required & The labor charges
  labor_hours, labor_charges = labor_calc(gallons_of_paint)

  #Calculate The total cost of the paint job
  total = total_cost(labor_charges,paint_cost)

  #Display the results
  print("\nThe number of gallons of paint required: ",format(gallons_of_paint,".2f"),"gallons")
  print("The hours of labor required :",format(labor_hours,".2f"))
  print("The cost of the paint : $",format(paint_cost,",.2f"))
  print("The labor charges : $",format(labor_charges,",.2f"))
  print("The total cost of the paint job : $",format(total,",.2f"))

# The get_values function prompts the
# user to enter the wall space, price of the paint and it
# returns that values.
def get_values():
  wall = float(input("Enter the square feet of wall space to be painted :"))
  paint = float(input("Enter the price of the paint per gallon :"))
  return wall, paint

# The paint_calc function accepts wall_space, paint_price
# as arguments and returns gallons_of_paint, paint_cost
# specified by Global costant PER_GALLON.
def paint_calc(wall_space, paint_price):
  gallons_of_paint = wall_space / PER_GALLON
  paint_cost = gallons_of_paint * paint_price
  return gallons_of_paint, paint_cost

# The labor_calc function accepts gallons_of_paint
# as arguments and returns labor_hours, labor_charges
# specified by Global costant LABOR_HOURS & PER_HOUR_LABOR_CHARGE.
def labor_calc(gallons_of_paint):
  labor_hours = gallons_of_paint * LABOR_HOURS
  labor_charges = labor_hours * PER_HOUR_LABOR_CHARGE
  return labor_hours, labor_charges

# The total_cost function accepts labor_charges and paint_cost
# as arguments and returns total
def total_cost(labor_charges,paint_cost):
  total = labor_charges + paint_cost
  return total
  
# Call the main function.
main()
