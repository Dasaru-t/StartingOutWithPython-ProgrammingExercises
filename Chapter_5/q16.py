#16. Odd/Even Counter

import random

def main():
    #display header
    print("Number\t\tEven/Odd")
    print("-"*24)

    # Initialize an accumulator variables.    
    total_even_numb = 0
    total_odd_numb = 0

    #get 100 random numbers
    for n in range(100):
        number = gen_numbers()

        #determine whether number is even or odd.
        if number % 2 == 0:
            status = "Evan"
            total_even_numb += 1
        else:
            status = "Odd"
            total_odd_numb += 1

        #display number and status
        print(number,"\t\t",status)

    #display even number count and odd number count
    print("\nThere are",total_even_numb,"even numbers and",total_odd_numb,"odd numbers")

#generate random number
def gen_numbers():
    number = random.randint(0, 1000)
    return number

# Call the main function.
main()