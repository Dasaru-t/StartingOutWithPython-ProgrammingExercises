# validate_password.py

# This program gets a password from the user and
# validates it.

import login_1

def main():
  # Get a password from the user.
  password = input('Enter your password: ')

  # Validate the password.
  while not login_1.valid_password(password):
    print('That password is not valid.')
    password = input('Enter your password: ')

  print('That is a valid password.')

# Call the main function.
main()