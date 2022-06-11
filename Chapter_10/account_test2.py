# account_test2.py

# This program demonstrates the BankAccount class
# with the _ _str_ _ method added to it.

import bankaccount2

def main():
    # Get the starting balance.
    start_bal = float(input('Enter your starting balance: '))

    # Create a BankAccount object.
    savings = bankaccount2.BankAccount(start_bal)