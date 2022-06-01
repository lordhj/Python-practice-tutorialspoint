num = int(input("Enter num: "))
first_dig = num
last_dig = num%10
while (first_dig>=10):
    first_dig = first_dig//10
print("First digit ",first_dig)
print("Last digit ", last_dig)