# 1. Total Sales

# WEEKDAYS is used as a constant for the
# size of the list.
WEEKDAYS = 7


def main():
    sales = get_sales()
    total = get_total(sales)
    print()

    # Display the total of the list elements.
    print('The total sales for the week is $',total)


def get_sales():
    # Create a list to hold sales
    sales = [0] * WEEKDAYS

    # Get sales for each day
    for day in range(WEEKDAYS):
        print("Enter a store's sales for day #", day + 1,': ',sep='',end='')
        sales[day] = float(input())

    # Return the list 
    return sales

def get_total(sales):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Calculate the total of the list elements
    for value in sales:
        total += value

    return total

# Call the main function.
main()



