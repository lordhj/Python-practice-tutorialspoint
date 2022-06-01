#Find HCF
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
while num2!=0:
    temp = num2
    num2=num1%num2
    num1 = temp
print(num1)