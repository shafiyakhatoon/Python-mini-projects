import math
def paintcount(height, width, coverage):
   area = height * width
   noofcans = math.ceil(area/coverage)
   print(f"No of cans required : {noofcans}")

height = int(input("Enter the height of the wall : "))
width = int(input("Enter the width of the wall : "))
coverage = 7
noofcans = 1
paintcount(height, width ,coverage )
