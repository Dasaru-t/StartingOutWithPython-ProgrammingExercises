# 11. Lo Shu Magic Square

def main():

  # constants for rows and columns
  ROWS = 3
  COLS = 3

  # create a two dimensional list.
  values = [[0,0,0],
            [0,0,0],
            [0,0,0]]

  print("Enter value for")
  for r in range(ROWS):
    for c in range(COLS):
      print("row",r + 1,"column",c + 1,end = "")
      values[r][c] = int(input(": "))
  
  #display the random numbers
  for r in range(ROWS):
    for c in range(COLS):
      print(values[r][c])     


main()