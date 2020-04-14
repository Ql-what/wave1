import math
radius = int(input("the radius of the cylinder:"))
height = int(input('the height of the cylinder:'))
pi = math.pi
basearea = pi*radius**2
volume = round(height*basearea, 1)
print('The volume of the cylinder is', volume)