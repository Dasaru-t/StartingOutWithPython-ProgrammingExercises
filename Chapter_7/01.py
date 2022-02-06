# 1. Total Sales

# WEEKDAYS is used as a constant for the
# size of the list.
WEEKDAYS = 7

def main():
  
  # Create a list to hold sales
  sales = [0] * WEEKDAYS

  # Create a variable to use as an accumulator.
  total = 0.0

  # Get sales for each day49.
  for day in range(WEEKDAYS):
    print('Enter a store’s sales for day ', day + 1,': ',sep='',end='')
    sales[day] = float(input())

  # Calculate the total of the list elements
  for value in sales:
    total += value

  # Display the total of the list elements.
  print('The total sales for the week is',total)

# Call the main function.
main()