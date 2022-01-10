# 15. Time Calculator

#asks the user to enter a number of seconds
seconds = int(input("Enter number of seconds: "))

if seconds >= 60 and seconds < 3600:
  time = seconds / 60
  status = "minutes"

elif seconds >= 3600 and seconds < 86400:
  time = seconds / 3600
  status = "hours"

elif seconds >= 86400:
  time = seconds / 86400
  status = "days"
else:
  time = seconds
  status = "seconds"


print(seconds,"seconds equal to",format(time,".2f"),status)