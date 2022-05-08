# 2. Capital Quiz

def main():
  # Create dictionarie
  states={'Alabama': 'Montgomery', 'Alaska': 'Juneau','Arizona':'Phoenix',
    'Arkansas':'Little Rock', 'California': 'Sacramento', 'Colorado':'Denver',
    'Connecticut':'Hartford', 'Delaware':'Dover','Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinios': 'Springfield', 'Indiana': 'Indianapolis','Iowa': 'Des Monies',
    'Kansas': 'Topeka','Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Neveda': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakoda': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

  # Initialize an accumulators
  right = 0
  wrong = 0

  # Get length of dictionarie
  count = len(states)

  for i in range(count):
    # Get randomly selected key-value pair as a tuple
    key,value = states.popitem()
    print("What is the capital of",key,"state",end = '')
    # Get user input
    answer = input("? ")

    # Check if answer is correct
    if answer.lower() == value.lower():
      right += 1
      print("Correct.")
      print("Total answers:",right + wrong)
      print("Correct answers: ",right)
      print("Incorrect answers: ",wrong,"\n")
    else:
      wrong += 1
      print("Wrong! correct answer is",value)
      print("Total answers:",right + wrong)
      print("Correct answers: ",right)
      print("Incorrect answers: ",wrong,"\n")
      
# Call the main function.      
main()