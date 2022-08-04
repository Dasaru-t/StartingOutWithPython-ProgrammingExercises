# This program passes a Coin object as
# an argument to a function.
import coin

# main function
def main():
    # Create a Coin object.
    my_coin = coin.Coin()

    # This will display 'Heads'.
    print(my_coin.get_sideup())

    # Pass the object to the flip function.
    flip(my_coin)

    # This might display 'Heads', or it might