sum = 0
print("Enter 10 numbers of your choice:")
for i in range(1,11):
    num = int(input("Enter number: "))
    sum = sum+num
avg=sum/10
print("SUM: ", sum)
print("AVG: ", avg)