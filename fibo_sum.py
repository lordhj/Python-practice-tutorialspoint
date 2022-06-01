first = 0
second = 1
num = int(input("Upto what: "))
print(first)
print(second)
sum = first+second
for i in range(2, num):
    third = first + second
    print(third)
    sum = sum + third
    first, second = second, third
print("SUM is ", sum)