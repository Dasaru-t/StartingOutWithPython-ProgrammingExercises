# 7. Driver’s License Exam

def main():
  # Create a list with correct answers
  correct_answers=["A", "C", "A", "A", "D",
                     "B", "C", "A", "C", "B",
                     "A", "D", "C", "A", "D",
                     "C", "B", "B", "D", "A"]

  # Get student answers & add it to a list
  student_answers = std_answers()

  # Check answers & Display results
  chk_answers(correct_answers, student_answers)


def std_answers():
  # Open my_file for for reading.
  my_file = open("answers.txt","r")

  # Read the lines from your file
  student_answers = my_file.readlines()

  # Strip all the \n from the elements
  index = 0  
  while index < len(student_answers):
    student_answers[index] = student_answers[index].rstrip("\n")
    index += 1

  # Display student answers list
  print("Student Answers")
  print(student_answers)
  return student_answers


def chk_answers(correct_answers, student_answers):

  # Create a variable to use as an accumulator.
  total = 0
  # Create a list to hold incorrect answers index
  incorrect = []
  
  # Check student answers
  for c in range(20):
    if correct_answers[c] == student_answers[c]:
      total += 1
    elif correct_answers[c] != student_answers[c]:
      incorrect.append(c + 1)      

  print()

  # Display exam results
  if total >= 15:
    print("You passed the exam!")
  else:
    print("You failed the exam!")


  # Display results
  print("Total number of correct answers:",total)
  print("Total number of incorrect answers:",20 - total)
  
  
  # Display incorrect answers index
  if len(incorrect) > 0:
    print("\nQuestion numbers of the incorrectly answered questions.")
    for values in incorrect:
      print(values)
      

  else:
    print("\nCongratulations! all of your answers are correct.")
           
     
# Call the main function
main()
