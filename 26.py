import math
a = int(input("Enter coefficient of x^2: "))
b = int(input("Enter coefficient of x^1: "))
c = int(input("Enter the constant value"))
d = b**2-4*a*c
if d>0:
    root = (-b + math.sqrt(d)/(2*a))
    root2 = (-b - math.sqrt(d)/(2*a))
    print("Roots are ", root, "and ", root2)
elif d==0:
    root = root2 = -b/(2*a)
    print("Equal roots: ", root)
else:
    root = root2 = -b/(2*a)
    img = math.sqrt(d)/(2*a)
    print("Roots are \n", root+img, "\n", root-img)
