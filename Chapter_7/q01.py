# 1. Total Sales

# NUM_DAYS is used as a constant for the
# size of the list.
NUM_DAYS = 7

def main():

  # Create a list to hold sales
  my_list = [0] * NUM_DAYS

  # Create a variable to use as an accumulator.
  total = 0.0

  # Get sales for each day
  for d in range(NUM_DAYS):
    sales = float(input("Enter sales for day #"+str(d+1)+" : "))
    my_list[d] = sales

  # Calculate the total of the list elements
  for values in my_list:
    total += values

  # Display the total of the list elements.
  print()
  print("Values: ",my_list)
  print('The total sales for the week is $',total)


# Call the main function.
main()