import math
num = int(input("Enter number: "))
sum = 0
sqr = math.pow(num, 2)
print("Square of digit is", sqr)
while sqr>0:
    rem = sqr%10
    sum = sum+rem
    sqr = sqr//10
print("Sum of digits", sum)
if sum == num:
    print("NEON")
else:
    print("NOT NEON")