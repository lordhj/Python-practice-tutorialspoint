import math
num = int(input("Enter number: "))
digits = []
dig = num
while dig>0:
    dig_rem = dig%10
    digits.append(dig_rem)
    dig = dig//10
sum=0
for i in digits:
    fact = math.factorial(i)
    print("Factorial of", i, "is ", fact)
    sum = sum + fact
if sum == num:
    print("Krishnamurthy")
else:
    print("Not Krishnamurthy number")