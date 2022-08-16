#Danial Syed
#syed0053
#CSCI 1133, Section 030
#Assignment 1
import math
b = float(input("Enter shorter side: "))
c = float(input("Enter other side: "))
A = float(input("Enter angle between sides in degrees (A): "))
A_radians = math.radians(A)
a = math.sqrt((b**2) + (c**2) - (2*b*c*math.cos(A_radians)))
x = b* (math.sin(A_radians))
y = x / a
z = math.asin(y)
B = math.degrees(z)
C = 180 - A - B
print("Enter shorter side (b):", b)
print("Enter angle between sides in degrees (A):", A)
print("Enter other side (c):", c)
print("Angle B is ", B)
print("Side a is ", a)
print("Angle C is ", C)
