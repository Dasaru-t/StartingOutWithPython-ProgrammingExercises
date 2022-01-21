# 7. Stadium Seating

#Global costant
CLASS_A_COST = 20
CLASS_B_COST = 15
CLASS_C_COST = 10

def main():
  #Get values
  class_a, class_b, class_c = get_values()

  #Calculate income
  class_a_income, class_b_income, class_c_income, total = calc_income(class_a, class_b, class_c)
  
  #Display the results
  print("\nClass A seats income :$",format(class_a_income,",.2f"))
  print("Class B seats income :$",format(class_b_income,",.2f"))
  print("Class C seats income :$",format(class_c_income,",.2f"))
  print("Total income :$",format(total,",.2f"))

# The get_value function prompts the
# user to enter the ticket amount and it
# returns that value.
def get_values():
  class_a = int(input("how many tickets for class A of seats were sold: "))
  class_b = int(input("how many tickets for class B of seats were sold: "))
  class_c = int(input("how many tickets for class C of seats were sold: "))
  return class_a, class_b, class_c

# The calc_income function accepts class_a, class_b, class_c
# as arguments and returns class_a_income, class_b_income, class_c_income & total
# specified by Global costant.
def calc_income(class_a, class_b, class_c):
  cl_a = class_a * CLASS_A_COST
  cl_b = class_b * CLASS_B_COST
  cl_c = class_c * CLASS_C_COST
  total = cl_a + cl_b + cl_c
  return cl_a, cl_b, cl_c, total
  
# Call the main function.
main()