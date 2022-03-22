# drop_lowest_score.py
# In the Spotlight: Processing a List

# This program gets a series of test scores and
# calculates the average of the scores with the
# lowest score dropped.

def main():

  # Get the test scores from the user.
  score = get_score()
  print("Scores: ",score)

  # Get the total of the test scores.
  total = get_total(score)
  print("Total: ",total)
  
  # Get the lowest test score.
  lowest = min(score)
  print("Lowest: ",lowest)

  # Subtract the lowest score from the total.
  total -= lowest
  print("Adjusted total: ",total)

  # Calculate the average. Note that we divide
  # by 1 less than the number of scores because
  # the lowest score was dropped.
  average = total / (len(score)-1)
  print("Average: ",average)


# The get_scores function gets a series of test
# scores from the user and stores them in a list.
# A reference to the list is returned.

def get_score():

  # Create an empty list.
  std_score = []

  # Create a variable to control the loop.
  another = "y"

  # Get the scores from the user and add them to
  # the list.
  while another == "y":

    # Get a score and add it to the list.
    score = int(input("Enter a test score: "))

    std_score.append(score)

    # Want to do this again?
    another = input("Do you want to enter another? (y = yes, anything else = no): ")

    print()

  # Return the list.
  return std_score

# The get_total function accepts a list as an
# argument returns the total of the values in
# the list.
def get_total(score):
  # Create a variable to use as an accumulator.
  total = 0

  # Calculate the total of the list elements.
  for i in score:
    total += i

  # Return the total.
  return total
  
# Call the main function.
main()
    