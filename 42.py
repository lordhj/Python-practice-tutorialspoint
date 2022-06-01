import math
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x = math.pow((x2-x1), 2)
y = math.pow((y2-y1), 2)
dist = math.sqrt(x+y)
print(dist)