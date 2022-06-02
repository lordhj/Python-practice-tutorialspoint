import math
def dig_sq_sum(num):
    while num> 0:
        rem = num%10
        sum = sum + math.pow(rem, 2)
        num = num//10
    return sum
num = int(input("Enter number: "))
temp = num
while temp!=1 and temp!=4:
    temp = dig_sq_sum(temp)
if temp ==1:
    print("Happy Number")
else:
    print("not a happy number")