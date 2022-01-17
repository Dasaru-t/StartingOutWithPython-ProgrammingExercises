# 1. Kilometer Converter

def main():
  # Get the number of km
  km = float(input("Enter a distance in kilometers: "))
  # Convert the km to miles
  kilometer_converter(km)

def kilometer_converter(kilometer):
  miles = kilometer * 0.6214
  print()
  print(kilometer,"kilometers equal to",format(miles,".2f"),"miles")

# Call the main function.
main()