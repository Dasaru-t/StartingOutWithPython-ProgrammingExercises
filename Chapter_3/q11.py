# 11. Book Club Points

# ask user to enter the number of books that he or she bought
books = int(input("Enter the number of books purchased this month: "))

if books <= 1:
  points = 0

elif books <= 3:
  points = 5

elif books <= 5:
  points = 15

elif books <= 7:
  points = 30

else:
  points = 60

print("you earned",points,"points for", books,"books you purchased")
