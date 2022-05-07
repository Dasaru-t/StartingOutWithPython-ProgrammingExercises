# 1. Course information

def main():
  # Create dictionaries
  room_number = {"CS101" : "3004","CS102" : "4501","CS103" : "6755","NT110" : "1244","CM241" : "1411"}
  
  instructor = {"CS101" : "Haynes","CS102" : "Alvarado","CS103" : "Rich","NT110" : "Burke","CM241" : "Lee"}
  
  meeting_time = {"CS101" : "8:00 a.m.","CS102" : "9:00 a.m.","CS103" : "10:00 a.m.","NT110" : "11:00 a.m.","CM241" : "1:00 p.m."}

  # Display Course Numbers
  print("Course Numbers")
  for key in room_number:
    print(key)

  print()
  # Get course number
  c_number = input("Enter a course number: ")

  print()
  # Display results
  print("Room Number: ",room_number[c_number],"\n","Instructor: ",instructor[c_number],"\n","Meeting Time: ",meeting_time[c_number],sep="")

# Call the main function
main()