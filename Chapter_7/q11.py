# 11. Lo Shu Magic Square

def main():

  # constants for rows and columns
  ROWS = 3
  COLS = 3

  # create a two dimensional list.
  values = [[0,0,0],
            [0,0,0],
            [0,0,0]]

  print("Enter numbers from 1 to 9")
  for r in range(ROWS):
    for c in range(COLS):
      print("row",r + 1,"column",c + 1,end = "")
      values[r][c] = int(input(": "))

  # Get the totals from functions and assign them to variables
  r1,r2,r3 = sum_of_rows(values)
  c1,c2,c3 = sum_of_cols(values)
  d1,d2 = sum_of_diagonal(values)
      
  
  #display the random numbers
  for r in range(ROWS):
    for c in range(COLS):
      print(values[r][c])     


# Get sum of rows
def sum_of_rows(values):
  r1 = 0
  for num in values[0]:
    r1 += num

  r2 = 0
  for num in values[1]:
    r2 += num
    
  r3 = 0
  for num in values[2]:
    r3 += num

  # Return values
  return r1,r2,r3


# Get sum of columns
def sum_of_cols(values):
  c1 = 0
  for num in range(3):
    c1 += values[num][0]

  c2 = 0
  for num in range(3):
    c2 += values[num][1]

  c3 = 0
  for num in range(3):
    c3 += values[num][2]

  # Return values
  return c1,c2,c3


# Get sum of diagonal
def sum_of_diagonal(values):
  d1 = 0
  for num in range(3):
    d1 += values[num][num]
    
  d2 = 0
  for num in range(3):
    d2 += values[num][2-num]

  # Return values
  return d1, d2


main()