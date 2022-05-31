maxnum = int(input("Enter maximum number: "))
minnum = int(input("Enter minimum number: "))
for i in range(minnum, maxnum+1):
    if i<0:
        continue
    else:
        print(i)