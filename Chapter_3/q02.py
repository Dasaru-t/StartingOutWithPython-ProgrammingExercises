# 2. Areas of Rectangles

#asks for the length and width of two rectangles.
print("Enter Rectangle 1 length and width")
rec1_length = float(input("Enter length of the rectangle 1: "))
rec1_width = float(input("Enter width of the rectangle 1 : "))
print()
print("Enter Rectangle 2 length and width")
rec2_length = float(input("Enter length of the rectangle 2: "))
rec2_width = float(input("Enter width of the rectangle 2 : "))

# calculate the areas
rec1_area = rec1_length * rec1_width
rec2_area = rec2_length * rec2_width

if rec1_area > rec2_area:
  print('\nRectangle 1 Area:',rec1_area , 'is bigger than Rectangle 2 Area:',rec2_area)
elif rec1_area < rec2_area:
  print('\nRectangle 2 Area:',rec2_area , 'is bigger than Rectangle 1 Area:',rec1_area)
else:
  print('\nRectangle 1 Area:',rec1_area , 'is equal to Rectangle 2 Area:',rec2_area)

