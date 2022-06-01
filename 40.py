sum = 0
for i in range(10):
    num = int(input("Number: "))
    if num<0:
        break
    sum = sum+num
print(sum)