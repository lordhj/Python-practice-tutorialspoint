num = int(input("Enter number: "))
count = 0
while(num>0):
    num = num//10
    count = count+1
print("Number of digits in a given number ", count)