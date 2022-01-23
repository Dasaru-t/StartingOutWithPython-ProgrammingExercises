# 13. Falling Distance

#Global costant
G = 9.8

def main():
  #display header
  print("Time(sec)\tDistance(m)")

  #loop that passes the values 1 through 10 as arguments(seconds)
  for time in range(1,11):
    distance = falling_distance(time)
    print(time,"\t\t",format(distance,".2f"))

# The falling_distance function accepts time
# as argument and returns distance
# specified by G
def falling_distance(time):
  distance = 0.5 * (G * (time**2))
  return distance

# Call the main function.
main()