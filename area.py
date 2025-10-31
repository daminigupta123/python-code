import math
r = 42      

theta = 60    
length = (theta / 360) * (2 * math.pi * r)
side = length / 4
area = side ** 2
print("Length of wire (arc):", round(length, 2))
print("Side of square:", round(side, 2))
print("Area of square:", round(area, 2))
