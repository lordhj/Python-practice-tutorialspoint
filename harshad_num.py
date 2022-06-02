num = int(input("Enter number: "))
digits = []
dig = num
while dig>0:
    dig_rem = dig%10
    digits.append(dig_rem)
    dig = dig//10
tot = sum(digits)
if num%tot ==0:
    print("Harshad number")
else:
    print("Not a harshad number")