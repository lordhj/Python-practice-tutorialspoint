num = int(input("Enter number: "))
count = 0
for i in range(2, (num//2)+1):
    if num%i==0:
        count = count + 1
        break
if count > 0:
    print("Not prime")
else:
    print("Prime")
