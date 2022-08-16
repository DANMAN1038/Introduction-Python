import math
c = 100
f = int((9/5)*(c)+32)
while f != c:
    c -= 1
    f = int((9/5)*(c)+32)
print("Celsius is: ", c)
print("Farhenheit is: ", f)
