a = int(input("Input degree: "))
print ("Output radian:" , a * (3.14 / 180))

b = int(input("Height: "))
c = int(input("Base, first value: "))
d = int(input("Base, second value: "))
print ("Expected Output:" , (c + d) / 2 * b)

import math 
e = int(input("Input number of sides: "))
f = int(input("Input the length of a side "))
print ("The area of the polygon is:" , (e * f ** 2) / (4 * math.tan(3.14 / e)))

g = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
print ("Expected Output:" , g * h)