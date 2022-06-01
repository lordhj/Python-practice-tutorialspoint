a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
if(a>b):
    max = a
else:
    max = b
while(True):
    if max%a==0 and max%b==0:
        val = max
        break
    max = max+1
print(val)  