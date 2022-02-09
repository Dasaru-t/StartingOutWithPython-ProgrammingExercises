# In the Spotlight: Processing a List
# drop_lowest_score.py

# This program gets a series of test scores and
# calculates the average of the scores with the
# lowest score dropped.

def main():
  # Get the test scores from the user.
  scores = get_scores()

  # Get the total of the test scores.
  total = get_total(scores)

  # Get the lowest test score.
  lowest = min(scores)

  # Subtract the lowest score from the total.
  total -= lowest

  # Calculate the average. Note that we divide
  # by 1 less than the number of scores because
  # the lowest score was dropped.
  average = total / (len(scores) - 1)

  # Display the average.
  print('The average, with the lowest score dropped is:', average)