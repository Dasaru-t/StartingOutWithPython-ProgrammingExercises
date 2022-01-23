# 15. Test Average and Grade

def main():

  #get scores
  score_1 = int(input("Enter test 1 score: "))
  score_2 = int(input("Enter test 2 score: "))
  score_3 = int(input("Enter test 3 score: "))
  score_4 = int(input("Enter test 4 score: "))
  score_5 = int(input("Enter test 5 score: "))

  #display header
  print("\nScore", "\t\t", "Grade")
  print("-"*22)

  #calculate average
  average = calc_average(score_1,score_2,score_3,score_4,score_5)

  #determine grade
  determine_grade(score_1,score_2,score_3,score_4,score_5)

  #display average
  print("\nYou'r score average is:",format(average,".2f"))

# The calc_average function accepts score_1,score_2,score_3,score_4 & score_5
# as arguments and average
def calc_average(score_1,score_2,score_3,score_4,score_5):
    average = (score_1 + score_2 + score_3 + score_4 + score_5) / 5
    return average

# The determine_grade function accepts score_1,score_2,score_3,score_4 & score_5
# as arguments   
def determine_grade(a,b,c,d,e):  
    for grade in (a,b,c,d,e):
      if grade <= 100 and grade > 89:
        print(grade, "\t\t", "A")
      elif grade < 90 and grade > 79:
        print(grade, "\t\t", "B")
      elif grade < 80 and grade > 69:
        print(grade, "\t\t", "C")
      elif grade < 70 and grade > 59:
        print(grade, "\t\t", "D")
      elif grade < 60 and grade >= 0:
        print(grade, "\t\t", "E")
      else:
        print("Enter a valid score! ")

# Call the main function.
main()