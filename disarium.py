num = int(input("ENter number: "))
length =len(str(num))
temp = num
sum, rem = 0

while temp>0:
    rem = temp%10
    sum = sum + int(rem**length)
    temp = temp//10
    length = length -1
print("SUM OF DIGITS: ", sum)
if sum == num:
    print("DISARIUM")
else:
    print("NOT DISARIUM")