from ast import Str


num = int(input("Enter number: "))
digits = []
dig = num
count = len(str(num))
total = 0
while dig>0:
    dig_rem = dig%10
    dig = dig//10
    dig_res = dig_rem**count
    total = dig_res+total
print(total)
if total==num:
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")